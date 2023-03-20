import math 
import config
import num

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
    return  mu + sd * math.sqrt(-2 * math.log( math.random() )) * math.cos(2 * math.pi * math.random())

def samples(t, n): 
    u = {}
    if n is None: 
        for i in range(1, len(t)): 
            u[i] = t[math.random(len(t))]
    else: 
        for i in range(1, n): 
            u[i] = t[math.random(len(t))]
    
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

    difference = math.abs(lt - gt) / n 
    return difference <= config.the['cliff']

def delta(i, other): 
    e, y, z = 1E-32, i, other
    num = math.abs(y.i["mu"] - z.i["mu"])
    den = (e + y.i["sd"]**2 / y.i["n"] + z.i["sd"]**2 / z.i["n"]) ** .5
    return num / den 

def bootstrap(y0, z0): 

    x, y, z, yhat, zhat = num.Num(), num.Num(), num.Num(), {}, {}
    for _, y1 in enumerate(y0): 
        num.add(x, y1)
        num.add(y, y1)
    for _, z1 in enumerate(z0): 
        num.add(x, z1)
        num.add(z, z1)
    xmu, ymu, zmu = x.i["mu"], y.i["mu"], z.i["mu"]

    yhat, zhat = {}, {}
    for _, y1 in enumerate(y0): 
        yhat[1 + len(yhat)] = y1 - ymu + xmu
    for _, z1 in enumerate(z0): 
        zhat[1 + len(zhat)] = z1 - zmu + xmu

    tobs = delta(y, z)
    n = 0 
    for ele in range(1, config.the["bootstrap"]): 
        if delta(num.Num(samples(yhat)), num.Num(samples(zhat))) > tobs: 
            n = n + 1
    val = n / config.the["bootstrap"]
    return val >= config.the["conf"]

def rx(t, s): 
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
    t = t.has if t.has else t        # TODO: not quite sure about this line here
    n = len(t) / 2
    if len(t) % 2 == 0 :
        return (t[n] + t[n + 1]) / 2
    else: 
        return t[n + 1]

def div(t): 
    t = t.has if t.has else t 
    val = len(t) / 10   
    return (t[val * 9] - t[val]) / 2.56

def merge(rx1, rx2): 
    rx3 = rx({}, rx1.name)
    for _, t in enumerate(zip(rx1.has, rx2.has)): #TODO this may be an issue, line 100 in stats.lua
        for _, x in enumerate(t): 
            rx3.has[1 + len(rx3.has)] = x
    
    sorted(rx3.has)
    rx3.n = len(rx3.has)
    return rx3

def scottKnow(rxs, all, cohen): 
    def merges(i, j): 
        out = rx({}, rxs[i].name)
        for k in range(i, j): 
            out = merge(out, rxs[j])
        return out
    
    def same(lo, cut, hi): 
        l = merges(lo, cut)
        r = merges(cut + 1, hi)
        x = cliffsDelta(l.has, r.has)
        if x == True: 
            return bootstrap(l.has, r.has)
        else: 
            return x
        
    def recurse(lo, hi, rank): 
        b4 = merges(lo, hi)
        best = 0
        for j in range(lo, hi): 
            if j < hi: 
                l = merges(lo, j)
                r = merges(j + 1, hi)
                now = ((l.n* (mid(l) - mid(b4))**2) + (r.n*(mid(r) - mid(b4))**2)) / (l.n + r.n)
                if now > best: 
                    if math.abs(mid(l) - mid(r)) >= cohen: 
                        cut, best = j, now
        if cut and not same(lo, cut, hi): 
            rank = recurse(lo, cut, rank) + 1
            rank = recurse(cut + 1, hi, rank)
        else: 
            for i in range(lo, hi): 
                rxs[i].rank = rank
        return rank
    
    sorted(rxs, key=lambda x, y: mid(x) < mid(y))
    cohen = div(merges(1, len(rxs))) * config.the["cohen"]
    recurse(1, len(rxs), 1)
    return rxs



