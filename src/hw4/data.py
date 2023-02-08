from cols import Cols
from row import Row
from lists import Lists
from string_util import *
from numerics import numerics
import config as config

class Data:
    '''Declares a data class that holds col and row data'''

    '''
    Parameters:
    src = location of the csv file to import from
    Attributes:
    cols = summary of data
    rows = list of rows
    '''
    def __init__(self, src):
        self.rows = list()
        self.cols = None
        if type(src) == str:
            csv(src, self.add)
        else:
            self.add(src or [])

    def add(self, t):
        '''
        Adds a row and appends to any columns
        :param t: row to add
        '''
        if self.cols:
            t = t if isinstance(t, Row) else Row(t)
            self.rows.append(t)
            self.cols.add(t)
        else:
            self.cols = Cols(t)

    def clone(self, init):
        '''
        Returns a clone
        :param init: Initial data for the clone
        '''
        data = Data(list(self.cols.names))
        list(map(data.add, init or []))
        return data

    def stats(self, cols, nPlaces, what):
        ''' 
        reports mid or div of cols (defaults to i.cols.y)
        '''
        return dict(sorted({col.txt: col.rnd(getattr(col, what)(), nPlaces) for col in cols or self.cols.y}.items()))

    # def better(self, row1, row2):
    #     '''
    #     Returns true if `row1` dominates
    #     '''
    #     s1,s2,ys = 0, 0, self.cols.y
    #     for _,col in enumerate(ys):
    #         x = col.norm(row1.cells[col.at])
    #         y = col.norm(row2.cells[col.at])
    #         s1 = s1 - math.exp(col.w * (x - y) / len(ys))
    #         s2 = s2 - math.exp(col.w * (y - x) / len(ys))
    #     return s1 / len(ys) < s2 / len(ys)

    def dist(self,row1,row2, cols = None):
        '''
        returns 0..1 distance `row1` to `row2`
        '''
        n,d = 0,0
        for _,col in enumerate(cols or self.cols.x):
            n = n + 1
            d = d + col.dist(row1.cells[col.at], row2.cells[col.at]) ** config.the['p']
        return (d/n) ** (1/config.the['p'])

    def around(self,row1,rows = None,cols = None):
        '''
        sort other `rows` by distance to `row`
        '''
        rows = rows if rows else self.rows
        cols = cols if cols else self.cols.x
        def func(row2):
            return {'row': row2, 'dist': self.dist(row1, row2, cols)}
            
        return sorted(list(map(func, rows)), key=lambda k: k['dist'])

    def furthest(self, row1, rows, cols, t): 
        t = self.around(row1, rows, cols)
        return t

    def half(self,rows=None,cols=None,above=None):
        '''
        divides data using 2 far points
        '''
        def project(row):
            return {"row": row, "dist": numerics.cosine(dist(row, A), dist(row, B), c)}
        def dist(row1, row2):
            return self.dist(row1, row2, cols)
        rows = (rows if rows else self.rows)
        some = Lists.many(rows, config.the["Sample"])
        A = Lists.any(some,above if above else config.the['seed'])
        B = self.around(A,some)[int(config.the["Far"] * len(rows)) // 1]["row"]
        c = dist(A,B)

        left, right = [], []

        for n, tmp in enumerate(sorted(list(map(project, rows)), key=lambda k: k["dist"])):
            if   n <= len(rows) // 2:
                left.append(tmp["row"])
                mid = tmp["row"]
            else:
                right.append(tmp["row"])
        return left, right, A, B, mid, c

    def cluster(self, rows  = None, min: int = None, cols = None, above: Row = None):
        '''
        returns `rows`, recursively halved
        :param rows: rows to cluster
        :param cols: cols to cluster
        '''
        rows = (rows if rows else self.rows)
        cols = (cols if cols else self.cols.x)
        node = {"data": self.clone(rows)}

        if len(rows) >= 2:
            left, right, node['A'], node['B'], node['mid'], _ = self.half(rows, cols, above)
            node['left'] = self.cluster(left, min, cols, node['A'])
            node['right'] = self.cluster(right, min, cols, node['B'])
        return node
    
    # def sway(self,rows = None,min = 0,cols = None,above = None):
    #     '''
    #     Returns best half, recursively
    #     '''
    #     rows = (rows if rows else self.rows)
    #     min  = min if min else len(rows) ** config.the["min"]
    #     cols = (cols if cols else self.cols.x)
    #     node = {"data": self.clone(rows)}
    #     if len(rows) > 2 * min:
    #         left, right, node['A'], node['B'], node['mid'], _ = self.half(rows, cols, above)
    #         if self.better(node['B'], node['A']):
    #             left, right, node['A'], node['B'] = right, left, node['B'], node['A']
    #         node['left'] = self.sway(left, min, cols, node['A'])
    #     return node
             
        


