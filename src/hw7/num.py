import math
import config as config

class Num():
    """
    Summarizes a stream of numbers. 
    """
    def __init__(self, t):
        self.i = {
            "n": 0, 
            "mu": 0, 
            "m2": 0, 
            "sd": 0
        }

        if t is None: 
            return self.i
        
        for _, x in enumerate(t): 
            self.add(x)
        
        return self.i

    def add(self, x) -> None:
        """
        Updates values needed for standard deviation
        """
        self.i["n"] = self.i["n"] + 1
        d = x - self.i["mu"]
        self.i["mu"] = self.i["mu"] + (d / self.i["n"])
        self.i["m2"] = self.i["m2"] + (d * (x - self.i["mu"]))
        if self.i["n"] < 2: 
            self.i["sd"] = 0
        else: 
            self.i["sd"] = (self.i["m2"] / (self.i["n"] - 1))**.5