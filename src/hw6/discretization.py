from copy import deepcopy
from math import inf, floor
from sym import Sym
import config as config


def bins(cols, rowss):
    out = []
    for col in cols:
        ranges = {}

        for y, rows in rowss.items():
            for row in rows:
                x = row.cells[col.at]
                if x != "?":
                    k = bin(col, x)
                    ranges[k] = ranges.get(k, RANGE(col.at, col.txt, x))
                    extend(ranges[k], x, y)

        ranges = list(dict(sorted(ranges.items())).values())
        r = ranges if isinstance(col, Sym) else merge_any(ranges)
        out.append(r)
    return out

def RANGE(at,txt,lo,hi=None):
    return {'at':at,'txt':txt,'lo':lo,'hi':lo or hi or lo,'y':Sym()}

def extend(range,n,s):
    range['lo'] = min(n, range['lo'])
    range['hi'] = max(n, range['hi'])
    range['y'].add(s)

def bin(col, x):
    if x == "?" or isinstance(col, Sym):
        return x
    tmp = (col.hi - col.lo) / (config.the["bins"] - 1)
    return 1 if col.hi == col.lo else floor(x / tmp + 0.5) * tmp

def merge_any(ranges0):
    def noGaps(t):
        for j in range(1,len(t)):
            t[j]['lo'] = t[j-1]['hi']
        t[0]['lo']  = float("-inf")
        t[len(t)-1]['hi'] =  float("inf")
        return t

    ranges1,j = [],0
    while j <= len(ranges0)-1:
        left = ranges0[j]
        right = None if j == len(ranges0)-1 else ranges0[j+1]
        if right:
            y = merge2(left['y'], right['y'])
            if y:
                j = j+1
                left['hi'], left['y'] = right['hi'], y
        ranges1.append(left)
        j = j+1
    return noGaps(ranges0) if len(ranges0)==len(ranges1) else merge_any(ranges1)


def merge2(col1, col2):
    new = merge(col1,col2)
    if new.div() <= (col1.div()*col1.n + col2.div()*col2.n)/new.n:
        return new

def merge(col1, col2):
    new = deepcopy(col1)
    if isinstance(col1, Sym):
        for n in col2.has:
            new.add(n)
    else:
        for n in col2.has:
            new.add(new,n)
        new.lo = min(col1.lo, col2.lo)
        new.hi = max(col1.hi, col2.hi)
    return new