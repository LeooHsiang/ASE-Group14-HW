import io
import math
import re

def rint(lo: float, hi: float):
    return math.floor(0.5 + rand(lo, hi))

def rand(self, lo, hi):
        """
        Generates pseudo-random number.
        :param lo: Lower limit
        :param hi: Higher limit
        :return: Pseudo-random number
        """
        lo, hi = lo or 0, hi or 1
        self.seed = (16807 * self.seed) % 2147483647
        return lo + (hi - lo) * self.seed / 2147483647

def rnd(n: float, n_places: int):
    """
    Rounds number n to n places.
    :param n: Number
    :param n_places: Number of decimal places to round
    :return: Rounded number
    """
    mult = math.pow(10, n_places or 3)
    return math.floor(n * mult + 0.5) / mult
