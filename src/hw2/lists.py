
class lists():
    # -- Note the following conventions for `map`.
    # -- - If a nil first argument is returned, that means :skip this result"
    # -- - If a nil second argument is returned, that means place the result as position size+1 in output.
    # -- - Else, the second argument is the key where we store function output.

    # map a function `fun`(v) over list (skip nil results)
    def map(self, t, fun):
        u = {}
        for k, v in t.items():
            v, k = fun(v)
            u[k or (1+len(u))] = v
        return u

    # map function `fun`(k,v) over list (skip nil results)
    def kap(self, t, fun):
        u = {}
        for k, v in t.items():
            v, k = fun(v)
            u[k or (1+len(u))] = v
        return u

    # sorted by `fun` (default= `<`)
    def sort(self, t, fun):
        t = sorted(t.items(), key=fun)
        return t

    # return list of table keys, sorted
    def function(self, k, _): return k

    def keys(self, t):
        u = self.kap(t, self.function)
        t = sorted(u.keys())
        return t

    def push(self, t, x):
        self[t] = x
