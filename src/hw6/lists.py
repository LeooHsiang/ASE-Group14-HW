import math
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

    def dkap(t, fun):
        u = {}
        for k,v in t.items():
            v, k = fun(k,v)
            u[k or len(u)] = v
        return u
    
    def kap2(table, fun):
        newTable = {}
        for k, v in table.items():
            v, k = fun(k, v)
            if k is None:
                newTable[len(newTable) + 1] = v
            else:
                newTable[k] = v
        return newTable
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
    
    def last(t):
        return t[len(t) - 1]
    
    def copy(t):
        return cp.deepcopy(t)

    def per(t): 
        p = 0.5
        p=math.floor(((p or .5)*len(t))+.5)
        return t[max(1,min(len(t),p))] 

    def slice(t, go=1, stop=1, inc=1):
        if go and go<0:
            go = len(t) + go
            return
        if stop and stop<0:
            stop = len(t) + stop
            return
        
        u = {}
        
        j = go
        while j <= stop :
            u[1+len(u)] = t[j]
            j += inc