
import math
from operator import itemgetter

from util import many
from row import Row
from cols import Cols
import config as config
import util as util
from string_util import *
import numerics as numerics
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

        return data

    def clone(self, init={}):
        data = Data([self.cols.names])
        _ = list(map(data.add, init))
        return data

    def dist(self,row1,row2, cols = None):
        '''
        returns 0..1 distance `row1` to `row2`
        '''
        n,d = 0,0
        for _,col in enumerate(cols or self.cols.x):
            n = n + 1
            d = d + col.dist(row1.cells[col.at], row2.cells[col.at]) ** config.the['p']
        return (d/n) ** (1/config.the['p'])

    # clustering rows into two sets 
    def half(self, rows=None, cols=None, above=None):
        def dist(row1, row2):
            return self.dist(row1, row2, cols)

        rows = rows or self.rows
        some = many(rows, config.the['Halves'])
        A = above or any(some)
        B = self.around(A, some)[int(config.the['Far'] * len(rows)) // 1]['row']
        c = dist(A, B)
        left, right = [], []

        def project(row):
            return {'row': row, 'dist': numerics.cosine(dist(row, A), dist(row, B), c)}

        for n, tmp in enumerate(sorted(list(map(project, rows)), key=itemgetter('dist'))):
            if n < len(rows) // 2:
                left.append(tmp['row'])
                mid = tmp['row']
            else:
                right.append(tmp['row'])
        return left, right, A, B, mid, c
    def around(self, row1, rows=None, cols=None):
        def function(row2):
            return {'row': row2, 'dist': self.dist(row1, row2, cols)}

        return sorted(list(map(function, rows or self.rows)), key=itemgetter('dist'))
    def tree(self, rows, cols, above, here): 
        rows = rows or self.rows 
        here = {'data': self.clone(rows)}
        if len(rows) >= 2 * len(self.rows) ^ config.the['min']: 
            left, right, A, B, c = self.half(rows, cols, above)
            here.left = self.tree(left, cols, A)
            here.right = self.tree(right, cols, B)
        return here 

    def showTree(self, tree, lvl, post): 
        if tree is not None: 
            lvl = lvl or 0 
            print("%s[%s] " % lvl, tree.data.rows) 
            if lvl == 0: 
                print(o(Data.stats(tree.data)))
            self.showTree(tree.left, lvl + 1)
            self.showTree(tree.right, lvl + 1)

    def sway(self, rows = None, min = None, cols = None, above = None):
        rows = rows or self.rows
        min = min or math.pow(len(rows), config.the['min'])
        cols = cols or self.cols.x
        node = {'data' : self.clone(rows)}
        if len(rows) > 2*min:
            left, right, node['A'], node['B'], node['mid'], _ = self.half(rows,cols,above)
            if self.better(node['B'],node['A']):
                left,right,node['A'],node['B'] = right,left,node['B'],node['A']
            node['left']  = self.sway(left,  min, cols, node['A'])
        return node
