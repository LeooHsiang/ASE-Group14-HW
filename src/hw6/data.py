
import math
from operator import itemgetter

from util import many, any
from row import Row
from cols import Cols
import config as config
import util as util
from string_util import *
from lists import Lists


class Data:
    '''Declares a data class that holds col and row data'''

    '''
    Parameters:
    src = location of the csv file to import from
    Attributes:
    cols = summary of data
    rows = list of rows
    '''
    def __init__(self,src):
        self.rows = []
        self.cols = None
        if isinstance(src, str):
            csv(src, self.add)
        else:
            for row in src:
                self.add(row)
    def add(self, t):
        if self.cols:
            t = Row(t) if type(t) == list else t
            self.rows.append(t)
            self.cols.add(t)
        else:
            self.cols = Cols(t)

    def stats(self, what, cols, nPlaces):
        def fun(_, col):
            if what == 'div':
                val = col.div()
            else:
                val = col.mid()
            return col.rnd(val, nPlaces), col.txt

        return Lists.kap(cols or self.cols.y, fun)

    def dist(self,row1,row2, cols = None):
        '''
        returns 0..1 distance `row1` to `row2`
        '''
        n, d = 0, 0
        c = cols or self.cols.x

        for col in c:
            n += 1
            d = d + col.dist(row1.cells[col.at], row2.cells[col.at]) ** config.the['p']
        return (d/n) ** (1/config.the['p'])

    # clustering rows into two sets 
    def half(self, rows=None, cols=None, above=None):
        def gap(r1, r2): 
            return self.dist(r1, r2, cols)
        def cos(a, b, c): 
            return ((a**2 + c**2 - b**2) / 2*c)
        def proj(r): 
            return {'row': r, 'x': cos(gap(r, A), gap(r, B), c)}
  
        rows = rows or self.rows
        some = many(rows, config.the['Halves'])
        A = above or any(some)
        def func(r): 
            return {'row': r, 'd': gap(r, A)}
        tmp = sorted(list(map(some, func())), 'd')
        far = tmp[len(tmp) * config.the['Far']]
        B = far['row']
        c = far['d']
        left, right = [], []

        for n, tmp in enumerate(sorted(list(map(rows, proj)), key=itemgetter('dist'))):
            if n < len(rows) // 2:
                left.append(tmp['row'])
                mid = tmp['row']
            else:
                right.append(tmp['row'])
        if config.the['Reuse']: 
            evals = 1
        else: 
            evals = 2

        return left, right, A, B, c, evals

    def tree(self, rows=None, cols=None, above=None):
        rows = rows or self.rows
        here = {'data': Data(self, rows)}
        
        if len(rows) >= 2 * len(self.rows) ** config.the['min']:
            left, right, A, B = self.half(rows, cols, above)
            here['left'] = self.tree(left, cols, A)
            here['right'] = self.tree(right, cols, B)
        return here

    def showTree(self, tree, lvl, post): 
        if tree: 
            lvl = lvl or 0
            print("%s[%s] |.." % (lvl, len(tree.data.rows)))
            if lvl == 0 or tree.left : 
                print(o(stats(tree.data)))
            self.showTree(tree.left, lvl + 1)
            self.showTree(tree.right, lvl + 1)

    def sway(self):
        data = self

        def worker(rows, worse, evals0=None, above=None):
            if len(rows) <= len(data.rows) ** config.the['min']:
                return rows, many(worse, config.the['rest'] * len(rows)), evals0
            else:
                l, r, A, B, c, evals = self.half(rows, cols, above)
                if self.better(B, A):
                    l, r, A, B = r, l, B, A
                for row in r:
                    worse.append(row)
                return worker(l, worse, evals + evals0, A)

        best, rest, evals = worker(data.rows, [], 0)
        return self.clone(best), self.clone(rest), evals
