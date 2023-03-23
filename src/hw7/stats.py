import math
from num import Num
import config
import random

def erf(x, a1, a2, a3, a4, a5, p, sign): 
    """
    -- from Abramowitz and Stegun 7.1.26 
    -- https://s3.amazonaws.com/nrbook.com/AandS-a4-v1-2.pdf
    -- (easier to read at https://en.wikipedia.org/wiki/Error_function#Approximation_with_elementary_functions)
    """
    a1, a2, a3, a4, a5 = 0.254829592, -0.284496736, 1.421413741, -1.453152027, 1.061405429
    p = 0.3275911

    sign = 1 
    if x < 0: 
        sign = -1
    
    x = math.abs(x)
    t = 1.0 / (1.0 + p*x)
    aa = (((((a5*t + a4)*t) + a3)*t + a2)*t + a1)
    y = 1.0 - aa * t * math.exp(-x * x)
    return sign * y 

def gaussian(mu, sd): 
    """return a sample from a Gaussian with mean `mu` and sd `sd`"""

    mu = mu if mu is not None else 0
    sd = sd if sd is not None else 1
    return  mu + sd * math.sqrt(-2 * math.log( random.random() )) * math.cos(2 * math.pi * random.random())

def samples(t, n = None): 
    u = []
    if n is None: 
        for i in range(1, len(t)): 
            u.append(random.choice(t))
    else: 
        for i in range(1, n): 
            u.append(random.choice(t))
    
    return u

def cliffsDelta(ns1, ns2): 
    """ bool; true if different by a trivial amount """
    n, gt, lt = 0, 0, 0 

    if len(ns1) > 128: 
        ns1 = samples(ns1, 128)
    if len(ns2) > 128: 
        ns2 = samples(ns2, 128)

    for _, x in enumerate(ns1):
        for _, y in enumerate(ns2): 
            n = n + 1 
            if x > y: 
                gt = gt + 1
            if x < y: 
                lt = lt + 1

    difference = abs(lt - gt) / n 
    return difference <= config.the['cliff']

def delta(i, other): 
    e, y, z = 1E-32, i, other
    num = abs(y.mu - z.mu)
    den = (e + y.sd **2 / y.n + z.sd **2 / z.n) ** .5
    return num / den 

def bootstrap(y0, z0): 
    x, y, z, yhat, zhat = Num(), Num(), Num(), [], []
    for y1 in y0:
        Num.add(x, y1)
        Num.add(y, y1)
    for z1 in z0:
        Num.add(x, z1)
        Num.add(z, z1)
    xmu, ymu, zmu = x.mu, y.mu, z.mu
    for y1 in y0: 
        yhat.append(y1 - ymu + xmu)
    for z1 in z0: 
        zhat.append(z1 - zmu + xmu)

    tobs = delta(y, z)
    n = 0
    for i in range(config.the['bootstrap']):
        if (delta(Num(samples(yhat)), Num(samples(zhat))) > tobs):
            n = n + 1
    return n / config.the['bootstrap'] > config.the['conf']
def RX(t, s): 
    sorted(t)
    r = {
        "name": s if s is not None else "", 
        "rank": 0, 
        "n" : len(t), 
        "show" : "", 
        "has" : t
    }
    return r 

def mid(t):
    t = t["has"] if "has" in t else t
    n = len(t) // 2
    if len(t) % 2 == 0 :
        return (t[n] + t[n + 1]) / 2
    else: 
        return t[n + 1]

def div(t):
    t = t["has"] if "has" in t else t
    val = len(t) // 10   
    return (t[val * 9] - t[val]) / 2.56

def merge(rx1, rx2):
    rx3 = RX([], rx1["name"])
    for t in (rx1["has"], rx2["has"]):
        for x in t:
            rx3["has"].append(x)
    rx3["has"].sort()
    rx3["n"] = len(rx3["has"])
    return rx3

def scottKnot(rxs): 
    def merges(i, j): 
        out = RX([], rxs[i]["name"])
        for k in range(i, j + 1):
            out = merge(out, rxs[j])
        return out
    
    def same(lo, cut, hi): 
        l = merges(lo, cut)
        r = merges(cut + 1, hi)
        x = cliffsDelta(l["has"], r["has"])
        if x == True:
            return bootstrap(l["has"], r["has"])
        else:
            return x
        
    def recurse(lo, hi, rank): 
        cut = None
        b4 = merges(lo, hi)
        best = 0
        for j in range(lo, hi + 1): 
            if j < hi: 
                l = merges(lo, j)
                r = merges(j + 1, hi)
                now = ((l["n"] * (mid(l) - mid(b4))**2) + (r["n"] *(mid(r) - mid(b4))**2)) / (l["n"]  + r["n"] )
                if now > best: 
                    if abs(mid(l) - mid(r)) >= cohen: 
                        cut, best = j, now
        if cut and not same(lo, cut, hi): 
            rank = recurse(lo, cut, rank) + 1
            rank = recurse(cut + 1, hi, rank)
        else: 
            for i in range(lo, hi + 1): 
                rxs[i]["rank"] = rank
        return rank
    
    rxs.sort(key=lambda x: mid(x))
    cohen = div(merges(0, len(rxs) - 1)) * config.the["cohen"]
    recurse(0, len(rxs) - 1, 1)
    return rxs

def tiles(rxs):
    """ss; makes on string per treatment showing rank, distribution, and values"""

    huge = math.inf
    lo, hi = huge, -math.inf
    for rx in rxs:
        lo, hi = min(lo, rx["has"][0]), max(hi, rx["has"][len(rx["has"]) - 1])
    for rx in rxs:
        t, u = rx["has"], []

        def of(x, most):
            return int(max(1, min(x, most)))

        def at(x):
            return t[of(len(t) * x//1, len(t))]

        def pos(x):
            return math.floor(of(config.the['width'] * (x - lo) / (hi - lo + 1E-32) // 1, config.the['width']))

        for i in range(0, config.the['width'] + 1):
            u.append(" ")
        a, b, c, d, e = at(.1), at(.3), at(.5), at(.7), at(.9)
        A, B, C, D, E = pos(a), pos(b), pos(c), pos(d), pos(e)

        for i in range(A, B + 1):
            u[i] = "-"
        for i in range(D, E + 1):
            u[i] = "-"

        u[config.the['width']//2] = "|"
        u[C] = "*"

        rx["show"] = rx["show"] + ''.join(u) + "{" + config.the["Fmt"].format(a)
        for x in [b, c, d, e]:
            rx["show"]= rx["show"] + ", " + config.the["Fmt"].format(x)
        rx["show"] = rx["show"] + "}"
    return rxs
