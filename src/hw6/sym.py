# SYM
# Summarize a stream of symbols.

import math

class Sym():
    """
    Stores details related to symbols in a CSV file
    """
    def __init__(self, at: int = 0, txt: str = "") -> None:
        super().__init__()
        # representing column position
        if at: 
            self.at = at
        else: 
            self.at = 0 
        # representing column name
        if txt: 
            self.txt = txt
        else: 
            self.txt = ""

        self.n = 0
        self.has = {}
        self.most = 0
        self.mode = None

    def add(self, x: str) -> None:
        """
            Method that adds the value in the column to the sym instance.
            Updates the maximum and mode value for the symbol. 
        """
        if x != "?":
            self.n = self.n + 1
            if x in self.has:
                self.has[x] = 1 + self.has[x]
            else:
                self.has[x] = 1
            if self.has[x] > self.most: 
                self.most = self.has[x]
                self.mode = x

    def mid(self) -> str:
        """
            Method that calculates mid value stored in the sym instance.
        """
        return self.mode


    def div(self, x = 0) -> float:
        """
            Method that calculates the entropy.
        """
        def fun(p: float) -> float: 
            return p * math.log2(p)

        e = 0
        for _, n in self.has.items():
            if n > 0:
                e = e + fun(n / self.n)
        return 0 - e

    def dist(self, s1, s2): 
        if s1 == "?" and s2 == "?": 
            return 1
        elif s1 == s2: 
            return 0
        else: 
            return 1