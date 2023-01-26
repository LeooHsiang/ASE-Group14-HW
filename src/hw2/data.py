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
       self.rows = []
       self.cols = None
       fun = lambda x: self.add(x)
       if "str" in str(type(src)):
            csv(src, fun)
       else:
            if src:
                Lists.map(src, fun)
            else:
                Lists.map({}, fun)

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

    def stats(self, cols,nplaces,what="mid"):
        def fun(k,col):
            return col.rnd((col,what)(),nplaces), col.txt
        return Lists.kap(fun,cols or self.cols.y)


