import re
import lists

class strings():

    # emulate printf
    # doesnt work correctly because string.format in python uses {} not % operators
    # fmt function not used because of above, instead where function is used, the 
    # formatting is done there
    def fmt(self, sControl, *argv):
        return sControl.format(*argv)

    # print `t` then return it
    def oo(self, t):
        print(self.o(t))
        return t

    # convert `t` to a string. sort named keys. 
    def o(self, t, isKeys):
        if (type(t) is dict):
            return t
        else:
            def func(k, v):
                if not str(t):
                    return ": {} {}".format(self.o(k), self.o(v)) 
            u = lists.kap(t, func)
            return sorted(u)
    
    # return int or float or bool or string from `s`
    def coerce(self, s):
        def func(s1):
            if re.search("^%s*(.-)%s*$", s):
                return True
            else:
                return False
        
        return int(s) or float(s) or func(s)
