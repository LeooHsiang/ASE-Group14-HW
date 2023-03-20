from num import Num
from sym import Sym

class Cols:
    '''Declares a column class that holds a column of data'''

    def __init__(self, t:dict):
        ''' 
        inits Cols with name of col
        :param names: (str) first row containing names of the columns
        :type names: (str) names of the columns
        :type all: (list[col]) every column including skipped columns are included here
        :type x: (list[col]) every independent unskipped column
        :type y: (list[col]) every dependent unskipped column
        :type klass: (col) single dependent col
        
        '''
        self.names = t
        self.all = []
        self.x = []
        self.y = []
        self.klass = None

        for col_name in t:
            if col_name[0].isupper():
                col = Num(t.index(col_name), col_name)
            else:
                col = Sym(t.index(col_name), col_name)
            self.all.append(col)

            if not col_name[-1] == "X":
                if "-" in col_name or "+" in col_name or "!" in col_name:
                    self.y.append(col)
                else:
                    self.x.append(col)
                if "!" in col_name:
                    self.klass=col

    def add(self, row):
        for t in [self.x, self.y]:
            for col in t:
                col.add(row.cells[col.at])

