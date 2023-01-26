from cols import Cols
from row import Row
from utilities import Utilities
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
    def __init__(self, src, fun):
        self.rows = []
        self.cols = None
        self.src=src

        if isinstance(src, str):
            utilities.csv(src, fun)
        else:
            for row in enumerate(src or []):
                self.add(row)
