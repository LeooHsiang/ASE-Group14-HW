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

    def stats(self, what, cols, nPlaces):
        def fun(_, cols):
            if what == 'div':
                val = cols.div()
            else:
                val = cols.mid()
            return cols.rnd(val, nPlaces),cols.txt
        return Lists.kap(cols or self.cols.y, fun)
        


