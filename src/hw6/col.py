import re
import math
import config as config

class Col:

    def __init__(self, n: int, s: str): 

        self.col = self.num(n, s) if s.find("[A-Z]") else self.sym(n, s)
        self.isIgnored = True if self.txt.find("X$") else False
        self.isKlass = True if self.txt.find("!$") else False
        self.isGoal = True if self.txt.find("[!+-]$") else False
        

    def add(self, x, n): 
        if x != "?": 
            n = n if n != None else 1
            self.n = self.n + n
            if self.isSym: 
                self.has[x] = n + self.has[x] if self.has[x] != None else n
                if self.has[x] > self.most: 
                    self.most = self.has[x]
                    self.mode = x
            else: 
                self.lo = min(x, self.lo)
                self.hi = max(x, self.hi)
                all = len(self.has)
                if all < config.the['Max']: 
                    pos = all + 1
                elif config.rand(None, None) < config.the['Max'] / self.n: 
                    pos = config.rint(1, all) 
                if pos: 
                    self.has[pos] = x
                    self.ok = False

    def adds(self, t): 
        for _, x in enumerate(t): 
            self.add(self, x, None)

        return self

    def extend(self, range, n, s): 
        range['lo'] = min(n, range['lo'])
        range['high'] = max(n, range['hi'])
        self.add(range['y'], s)
        
 
                