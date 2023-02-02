import math
import config


class numerics():
    # a float "x" lo<=x < x
    def rand(lo, hi):
        if not lo:
            lo = 0

        if not hi:
            hi = 1

        config.Seed = (16807 * config.Seed) % 2147483647

        return lo + (hi - lo) * config.Seed / 2147483647
      # a integer lo..hi-1

    def rint(self, lo, hi):
        return math.floor(0.5 + self.rand(lo, hi))
    # return `n` rounded to `nPlaces`

    def rnd(n, nPlaces=3):
        mult = 0
        if nPlaces:
            mult = 10 ** nPlaces
        else:
            mult = 10 ** 3

        return math.floor(n * mult + 0.5) / mult

    def cosine(self, a,b,c):
        x1 = (a**2 + c**2 - b**2) / (2**c)
        x2 = max(0, min(1, x1))
        y  = (a**2 - x2**2)**.5
        return x2, y

