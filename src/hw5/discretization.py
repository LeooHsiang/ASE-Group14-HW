from math import inf, floor
from row import Row
from col import Col
import config as config
import util as util
from creation import *

def bins(cols, rowss):
    out = []
    for col in cols:
        ranges = {}

        for y, rows in rowss.items():
            for row in rows:
                x = row.cells[col.at]
                if x != "?":
                    k = bin(col, x)
                    ranges[k] = ranges.get(k, Range(col.at, col.txt, x))
                    extend(ranges[k], x, y)

        ranges = (sorted(ranges.items(), key=lambda x: x[1].lo))
        ranges = [r[1] for r in ranges]
        out.append(ranges if isinstance(col, Sym) else merge_any(ranges))
    return out

def bin(col, x):
    if x == "?" or isinstance(col, Sym):
        return x
    tmp = (col.hi - col.lo) / (config.the["bins"] - 1)
    return 1 if col.hi == col.lo else floor(x / tmp + 0.5) * tmp

def merge_any(ranges0):
    def no_gaps(t):
        for j in range(1, len(t)):
            t[j].lo = t[j - 1].hi

        t[0].lo = -float("inf")
        t[-1].hi = float("inf")
        return t

    ranges1 = []
    j = 0

    while j < len(ranges0):
        left = ranges0[j]
        right = ranges0[j + 1]  if j + 1 < len(ranges0) else None
        if right is not None:
            y = merge2(left.y, right.y)
            if y is not None:
                j += 1
                left.hi, left.y = right.hi, y

        ranges1.append(left)
        j += 1
    return noGaps(ranges0) if len(ranges0) == len(ranges1) else merge_any(ranges1)

