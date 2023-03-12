from typing import List, Dict, Tuple
from data import *
from discretization import *
import util as util


def xpln(self, data, best, rest):
    def v(has):
        return value(has, len(best.rows), len(rest.rows), "best")
        
    def score(self, ranges: List[Range]):
        rule = self.rule(ranges, self.max_sizes)
        if rule:
            oo(showRule(rule))
            bestr = selects(rule, self.best.rows)
            restr = selects(rule, self.rest.rows)
            if len(bestr) + len(restr) > 0:
                return value({"best": len(bestr), "rest": len(restr)}, len(self.best.rows), len(self.rest.rows), "best"), rule
        return None,None

    tmp, self.max_sizes = [],{}
    for _,ranges in enumerate(bins(data.cols.x,{"best":best.rows, "rest":rest.rows})):
        self.max_sizes[ranges[0].txt] = len(ranges)
        print()
        for _,range in enumerate(ranges):
            print(range.txt, range.lo, range.hi)
            tmp.append({"range":range, "max":len(ranges), "val": v(range.y.has)})
    rule,mos = self.firstN(sorted(tmp, key = lambda k: k['val'],reverse=True), self.score)
    return rule,most


def firstN(self, sortedRanges: List[Tuple[Range, int, float]], scoreFun):
        print()
        for r in sortedRanges:
            print(r['range'].txt, r['range'].lo, r['range'].hi, rnd(r['val']), dict(r['range'].y.has))
        first = sortedRanges[0]['val']

        def useful(range):
            if range['val'] > 0.05 and range['val'] > first / 10:
                return range
        sortedRanges = [s for s in sortedRanges if useful(s)]
        most = -1
        out = -1

        for n in range(len(sortedRanges)):
            tmp, rule = scoreFun([r['range'] for r in sortedRanges[:n+1]])

            if tmp is not None and tmp > most:
                out, most = rule, tmp

        return out, most

def selects(rule, rows):
    def disjunction(ranges, row, x):
        for r in ranges:
            at = r['at']
            lo = r['lo']
            hi = r['hi'] 
            x = row.cells[at] 
            if x == '?' or (lo == hi and lo == x) or (lo <= x and x< hi):
                return True
        return False

    def conjunction(row):
        for _,ranges in rule.items():
            if not disjunction(ranges, row):
                return False
        return True
        
    def function(r):
        return r if conjunction(r) else None
    
    r = []
    for item in list(map(function, rows)):
        if item:
            r.append(item)
    return r


def show_rule(rule):
    
    def pretty(range):
        return range["lo"] if range["lo"] == range["hi"] else [range["lo"], range["hi"]]
    
    def merges(attr, ranges):
        return list(map(merge(sorted(ranges, key=lambda k: k["lo"])), pretty)), attr
    
    def merge(t0):
        j = 0
        t = []
        while j < len(t0):
            left = t0[j]
            right = t0[j+1]
            if right and left["hi"] == right["lo"]:
                left["hi"] = right["hi"]
                j = j +  1
            t.append({"lo": left["lo"], "hi": left["hi"]})
            j = j +  1

        return t if len(t0) == len(t) else merge(t)
    return kap(rule, merges)
