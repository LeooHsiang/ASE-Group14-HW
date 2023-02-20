
import math 

from row import Row
import config as config
import util as util


class Data:
    '''Declares a data class that holds col and row data'''

    '''
    Parameters:
    src = location of the csv file to import from
    Attributes:
    cols = summary of data
    rows = list of rows
    '''
    def __init__(self):
        self.rows = list()
        self.cols = None
    
    def read(self, sfile, data):  
        data = Data() 
        csv(sfile, function(t) row(data, t)))

        return data

    def clone(self, data, ts, data1): 
        data1 = row(Data(), data.cols.names)
        for i in ts: 
            row(data1, i)
        return data1

    def dist(self,t1,t2, cols = None, d, n, dist1):
        '''
        returns 0..1 distance `row1` to `row2`
        '''
        def dist1(col, x, y): 
            if x == "?" and y == "?": 
                return 1
            if col.isSym: 
                if x == y : 
                    return 0 
                else: 
                    return 1
            else: 
                x = norm(col, x)
                y = norm(col, y)
                if x == "?": 
                    x = 1 
                if y == "?": 
                    y = 1
                return math.abs(x - y)
        d, n = 0, 1 / float('inf')
        for _,col in enumerate(cols or self.cols.x):
            n = n + 1
            d = d + col.dist(t1.cells[col.at], t2.cells[col.at]) ** config.the['p']
        return (d/n) ** (1/config.the['p'])

    # clustering rows into two sets 
    def half(self,rows=None,cols=None,above=None):
            '''
            divides data using 2 far points
            '''
            def gap(r1, r2): 
                return self.dist(self, r1, r2, cols)
            def cos(a, b, c): 
                return (a^2 + c^2 - b^2) / (2 * c) 
            def project(r):
                return {'row' : r, 'x' : cos(gap(r, A), gap(r, B), c)}
            rows = rows or self.rows
            some = util.many(rows, config.the['Halves']) # what is this calling
            A    = above or util.any(rows)
            tmp = util.sort(map(some, function(r) return {'row': r, 'd': gap(r, A)}), "d")

            B = self.furthest(A, rows)['row']
            c = gap(A,B)
            left, right = [], []
            for n,tmp in enumerate(sorted(list(map(project, rows)), key=itemgetter('x'))):
                if n < len(rows)//2:
                    left.append(tmp['row'])
                    mid = tmp['row']
                else:
                    right.append(tmp['row'])
            return left, right, A, B, c

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
                print(o(stats(tree.data)))
            self.showTree(tree.left, lvl + 1)
            self.showTree(tree.right, lvl + 1)