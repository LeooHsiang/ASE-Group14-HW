from numerics import numerics
from sym import Sym
from num import Num
from data import Data
from string_util import *
from util import *
import config as config

def show_settings():
    print(config.the)


def test_rand():
    num1, num2 = Num(), Num()
    config.Seed = config.the["seed"]
    for i in range(1,10**3+1):
        num1.add(numerics.rand(0,1))
    config.Seed = config.the["seed"]
    for i in range(1,10**3+1):
        num2.add(numerics.rand(0,1))
    m1,m2 = numerics.rnd(num1.mid(),1), numerics.rnd(num2.mid(),1)
    return m1==m2 and .5 == numerics.rnd(m1,1)

    m1, m2 = round(num1.mid(), 10), round(num2.mid(), 10)
    return m1 == m2 and .5 == round(m1, 1)


def test_syms():
    sym = Sym()
    for x in ["a", "a", "a", "a", "b", "b", "c"]:
        sym.add(x)
    return "a" == sym.mid() and 1.379 == rnd(sym.div(), 3)


def test_nums():
    num = Num()
    for x in [1, 1, 1, 1, 2, 2, 3]:
        num.add(x)
    return 11 / 7 == num.mid() and 0.787 == rnd(num.div(), 3)


def test_read_csv(): 
    n=0
    def f(t):
        nonlocal n
        n += len(t)
    csv(config.the['file'],f)
    return n==8*399
def test_read_data_csv(): 
    data=Data(config.the['file'])
    return len(data.rows)==398 and \
    data.cols.y[1].w == -1 and \
    data.cols.x[1].at==1 and \
    len(data.cols.x)==4

def test_stats_data(): 
    data = Data(config.the['file'])
    d = {'y': data.cols.y, 'x': data.cols.x}
    for k, cols in d.items():
        print(k + 'mid'+ str(data.stats('mid', cols, 2)))
        print(''+ 'div' +str(data.stats('div', cols, 2)))