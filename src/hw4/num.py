from numerics import numerics
class Num():
    """
    Summarizes a stream of numbers. 
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
        self.mu = 0
        self.m2 = 0
        self.lo = float('inf')
        self.hi = float('-inf')
        if self.txt.find("-$"): 
            self.w = -1
        else: 
            self.w = 1

    def add(self, n: float) -> None:
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


    def rnd(self, x, n): 
        """
            Method that returns x unchanged, rounded 
        """
        if x == "?": 
            return x
        else: 
            return numerics.rnd(x, n)

    def norm(self, n): 
        """
            provides a normalized version of the numbers
        """
        if n == "?": 
            return n 
        else: 
            return (n - self.lo) / (self.hi - self.lo + (10**-32))

    def dist(self, n1, n2): 
        if n1 == "?" and n2 == "?": 
            return 1
        else: 
            n1 = self.norm(n1)
            n2 = self.norm(n2)
            if n1 == "?" and n2 < .5: 
                n1 = 1
            else: 
                n1 = 0
            if n2 == "?" and n1 < .5: 
                n2 = 1
            else: 
                n2 = 0 
            
            return abs(n1 - n2)