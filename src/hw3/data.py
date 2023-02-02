from cols import Cols
from row import Row
from lists import Lists
from string_util import *
import math

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
            map(src, self.add)

    def add(self, t):
        '''
        Adds a row and appends to any columns
        :param t: row to add
        '''
        if self.cols:
            t = t if "ROW" in str(type(t)) else Row(t)
            self.rows.append(t)
            self.cols.add(t)
        else:
            self.cols = Cols(t)

    def clone(self, init, data):
        '''
        Returns a clone
        :param init: Initial data for the clone
        '''
        data = Data(list(self.cols.names))
        Lists.map(init or [], self.add)
        return data

    def stats(self, what, cols, nPlaces, fun):
        ''' 
        reports mid or div of cols (defaults to i.cols.y)
        '''
        def fun(k, cols):
            return col.rnd((col,what)(),nplaces), col.txt
        return Lists.kap(cols or self.cols.y, fun)

    def better(self, row1, row2, s1, s2, ys, x, y):
        '''
        Returns true if `row1` dominates
        '''
        s1,s2,ys = 0, 0, self.cols.y
        for _,col in enumerate(ys):
            x = Num.norm(row1.cells[col.at])
            y = Num.norm(row2.cells[col.at])
            s1 = s1 - math.exp(col.w * (x - y) / len(ys))
            s2 = s2 - math.exp(col.w * (y - x) / len(ys))
        return s1 / len(ys) < s2 / len(ys)

    def dist(self,row1,row2,  cols, n, d):
        '''
        returns 0..1 distance `row1` to `row2`
        '''
        n,d = 0,0
        for _,col in enumerate(cols or i.cols.x):
            n = n + 1
            d = d + col.dist(row1.cells[col.at], row2.cells[col.at]) ** self.the['p']
        return (d/n) ** (1/self.the['p'])

    def around(self,row1,rows,cols):
        '''
        sort other `rows` by distance to `row`
        '''
        rows = rows if rows else self.rows
        cols = cols if cols else self.cols.x
        def func(row2):
            return {'row': row2, 'dist': self.dist(row1, row2, cols)}
            
        return sorted(list(map(func, rows)), key=lambda k: k['dist'])

    def half(self,rows,cols,above):
        '''
        divides data using 2 far points
        '''
        def project():
            return {"row": row, "dist": cosine(dist(row, A), dist(row, B), c)}
        def dist():
            return self.dist(row1, row2, cols)
        rows = (rows if rows else self.rows)
        some = many(rows, self.the["Sample"])
        A = above or any(some)
        B = self.around(A,some)[int(self.the["Far"] * len(rows)) // 1]["row"]
        c = dist(A,B)

        left, right = [], []

        for n, tmp in enumerate(sort(map(rows, project), key=lambda k: k["dist"])):
            if   n <= len(rows) // 2:
                left.append(tmp["row"])
                mid = tmp["row"]
            else:
                right.append(tmp["row"])
        return left, right, A, B, mid, c

    def cluster(self,rows,min,cols,above):
        '''
        returns `rows`, recursively halved
        :param rows: rows to cluster
        :param cols: cols to cluster
        '''
        rows = (rows if rows else self.rows)
        min  = min if min else len(rows) ** options["min"]
        cols = (cols if cols else self.cols.x)
        node = {"data": self.clone(rows)}

        if len(rows) > 2 * min:
            left, right, node.A, node.B, node.mid = self.half(rows, cols, above)
            node.left = self.cluster(left, min, cols, node.A)
            node.right = self.cluster(right, min, cols, node.B)
        return node
    
    def sway(self,rows,min,cols,above):
        '''
        Returns best half, recursively
        '''
        rows = (rows if rows else self.rows)
        min  = min if min else len(rows) ** options["min"]
        cols = (cols if cols else self.cols.x)
        node = {"data": self.clone(rows)}
        if len(rows) > 2 * min:
            left, right, node.A, node.B, node.mid = self.half(rows, cols, above)
            if self.better(node.B, node.A):
                left, right, node.A, node.B = right, left, node.B, node.A
            node['left'] = self.sway(left, min, cols, node.A)
        return node

    def show(self, node, what, cols, nPlaces, lvl) -> None: 
        """
            Prints the tree generated from the Data:tree method
            Notes on transition: 
                rep(lvl) repeats the previous string lvl number of times 
                #takes the length of the following value
                .. concatanates two strings together 
        """
        if node: 
            if lvl is None:
                lvl = 0
            for i in range(0, lvl): 
                print("| ", end = "")
            print(len(self.rows), end = "  ")

            if not node.left or lvl == 0: 
                print(self.stats(self, "mid",node.data.cols.y,nPlaces))
            
            # recursive call 
            self.show(node.left, what, cols, nPlaces, lvl+1)
            self.show(node.right, what, cols, nPlaces, lvl+1)

             
        


