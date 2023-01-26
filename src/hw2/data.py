from src.cols import Cols
from src.row import Row
from src.util import kap, map, csv
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
        if isinstance(src, str):
            csv(src, self.add)
        else:
            map(src or {},self.add) 

    def add(self, t):
        '''
        Adds a row and appends to any columns
        :param t: row to add
        '''
        if self.cols:
           t = t.cells and t or Row(t)
           self.rows.append(t)
           self.cols.add(t)
        else:
            self.cols = Cols(t)

    def clone(self, init, data):
        data = DATA(list(self.cols.names))
        map(init or [], self.add)
        return data

    def stats(self, cols, nPlaces, what="mid"):
        '''
        Shows stats for each col based on input function
        :param places: rounding int
        :param cols: list of columns
        :param what: function to apply to each column
        :return: dictionary of column stats
        '''
        def fun(k, col):
            return col.rnd((col,what)(),nplaces), col.txt
        return kap(cols or self.cols.y, fun)


