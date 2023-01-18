import math


class numerics():

    Seed = 937162211

    # a integer lo..hi-1
    def rint(self, lo, hi):
        return math.floor(0.5 + self.rand(lo, hi))

    # a float "x" lo<=x < x
    def rand(self, lo, hi):
        global Seed
        lo = lo or 0
        hi = hi or 1
        Seed = (16807 * Seed) % 2147483647
        return lo + (hi-lo) * Seed / 2147483647

    # return `n` rounded to `nPlaces`
    def rnd(self, n, nPlaces):
        mult = 10 ^ (nPlaces or 3)
        return math.floor(n * mult + 0.5) / mult
