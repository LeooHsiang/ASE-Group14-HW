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
        data = Data(list(self.cols.names))
        Lists.map(init or [], self.add)
        return data

    # def stats(self, what, cols, nPlaces, fun):
    #     def fun(k, cols):
    #         dict(sorted({col.txt: col.rnd(getattr(col, what)(), nplaces)
    #     return Lists.kap(cols or self.cols.y, fun)

    def better(self, row1, row2, s1, s2, ys, x, y):
        s1,s2,ys = 0, 0, self.cols.y
        for _,col in enumerate(ys):
            x = Num.norm(row1.cells[col.at])
            y = Num.norm(row2.cells[col.at])
            s1 = s1 - math.exp(col.w * (x - y) / len(ys))
            s2 = s2 - math.exp(col.w * (y - x) / len(ys))
        return s1 / len(ys) < s2 / len(ys)

    def dist(self,row1,row2,  cols, n, d):
        n,d = 0,0
        for _,col in enumerate(cols or i.cols.x):
            n = n + 1
            d = d + col.dist(row1.cells[col.at], row2.cells[col.at]) ** self.the['p']
        return (d/n) ** (1/self.the['p'])

    def around(self,row1,rows,cols):
        def func(row2):
            return {'row': row2, 'dist': self.dist(row1, row2, cols)}
            
        return sorted(list(map(func, rows)), key=lambda k: k['dist'])

    def half(self,rows,cols,above):
        def project():
            return
        def dist():
            return 
    # def cluster():
    
    # def sway():

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

             
        


