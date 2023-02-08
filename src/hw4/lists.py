import random
import config as config
import copy as cp

class Lists():
    # -- Note the following conventions for `map`.
    # -- - If a nil first argument is returned, that means :skip this result"
    # -- - If a nil second argument is returned, that means place the result as position size+1 in output.
    # -- - Else, the second argument is the key where we store function output.

    # map a function `fun`(v) over list (skip nil results)
    def map(t, fun):
        u = {}
        for k, v in t.items():
            v, k = fun(v)
            u[k or (1+len(u))] = v
        return u

    # map function `fun`(k,v) over list (skip nil results)
    def kap(t, fun):
        u = {}
        for v in t:
            k = t.index(v)
            v, k = fun(k,v) 
            u[k or len(u)] = v
        return u

    # sorted by `fun` (default= `<`)
    def sort(t, fun):
        t = sorted(t.items(), key=fun)
        return t

    # return list of table keys, sorted
    def function(k, _): return k

    def keys(self, t):
        u = self.kap(t, self.function)
        t = sorted(u.keys())
        return t

    def push(self, t, x):
        self[t] = x
    
    def any(t, seed = config.Seed):
        random.seed(seed)
        return random.choices(t)[0]
    
    def many(t,n,seed = config.Seed):
        random.seed(seed)
        return random.choices(t, k=n)
    
    def last(self, t):
        return t[len(t)]
    
    def copy(t):
        return cp.deepcopy(t)