import math
import random
import re

class Num():
    """
    Summarizes a stream of numbers. 
    """
    def __init__(self) -> None:
        super().__init__()
        self.n = 0
        self.mu = 0
        self.m2 = 0
        self.lo = float('inf')
        self.hi = float('-inf')

    def add(self, n) -> None:
        """
        Updates values needed for standard deviation
        """
        if str(n) != "?":
            self.n = self.n + 1
            d = n - self.mu
            self.mu = self.mu + (d / self.n)
            self.m2 = self.m2 + (d * (n - self.mu))
            self.lo = min(n, self.lo)
            self.hi = max(n, self.hi)

    def mid(self) -> float:
        """
        Get Central tendancy. 
        Returns: median of nums in Nums class
        """
        return self.mu

    def div(self) -> float:
        """
        Gets standard deviation using Welford's algorithm http://t.ly/nn_W
        """
        d = self.m2 / (self.n - 1)
        d = d ** .5 

        if self.m2 < 0: 
            return d
        else: 
            if self.n < 2: 
                return 0
            else:
                return d


