import math
from config import *

class numerics():
    


    # a float "x" lo<=x < x
    def rand(lo, hi):
        global Seed
        lo = lo or 0
        hi = hi or 1
        Seed = (16807 * Seed) % 2147483647
        return lo + (hi-lo) * Seed / 2147483647
      # a integer lo..hi-1
    def rint(self, lo, hi):
        return math.floor(0.5 + self.rand(lo, hi))
    # return `n` rounded to `nPlaces`
    def rnd(n, nPlaces = 3):
        mult = 10 ^ nPlaces
        return math.floor(n * mult + 0.5) / mult
