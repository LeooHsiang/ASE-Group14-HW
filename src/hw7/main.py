import math 
import config

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


