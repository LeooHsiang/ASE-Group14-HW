from numerics import numerics
from string_util import *
from num import Num
from util import *
from sym import Sym
import config as config
from data import Data

def show_settings():
    print(config.the)



def test_syms():
    sym = Sym()
    for x in ["a","a","a","a","b","b","c"]:
        sym.add(x)
    return "a" == sym.mid() and 1.379 == numerics.rnd(sym.div())

def test_nums():
    num = Num()
    for x in [1,1,1,1,2,2,3]:
        num.add(x)
    return 11/7 == num.mid() and 0.787 == numerics.rnd(num.div())

def test_repCols():
    t = repCols(dofile(config.the['file'])['cols'])
    _ = list(map(oo, t.cols.all))
    _ = list(map(oo, t.rows))

def test_synonyms():
    data = Data(config.the['file'])
    cols = dofile(config.the['file'])['cols']
    t = repCols(cols)
    node = t.cluster()
    show(node,"mid",data.cols.all,1)
    
def test_repRows():
    t=dofile(config.the['file'])
    rows = repRows(t, transpose(t['cols']))
    _ = list(map(oo, rows.cols.all))
    _ = list(map(oo, rows.rows))

def test_prototypes():
    t = dofile(config.the['file'])
    rows = repRows(t, transpose(t['cols']))
    show(rows.cluster(),"mid",rows.cols.all,1)

def test_position():
    t = dofile(config.the['file'])
    rows = repRows(t, transpose(t['cols']))
    rows.cluster()
    repPlace(rows)

def test_every():
    repgrid(config.the['file'])