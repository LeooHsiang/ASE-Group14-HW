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

def test_clone():
    data1 = Data(config.the["file"])
    data2 = data1.clone(data1.rows)

    return (
        len(data1.rows) == len(data2.rows)
        and data1.cols.y[1].w == data2.cols.y[1].w
        and data1.cols.x[1].at == data2.cols.x[1].at
        and len(data1.cols.x) == len(data2.cols.x)
    )

def test_around():
    data=Data(config.the['file'])
    print(0,0,data.rows[0].cells)
    for n,t in enumerate(data.around(data.rows[0])):
        if (n+1) %50 ==0:
            print(n, rnd(t['dist'],2) ,t['row'].cells)
            
def test_half():
    data=Data(config.the['file'])
    left,right,A,B,mid,c = data.half() 
    print(len(left),len(right),len(data.rows))
    print(A.cells,c)
    print(mid.cells)
    print(B.cells)

def test_cluster():
    data = Data(config.the['file'])
    show(data.cluster(), "mid", data.cols.y, 1)
    

def test_optimize():
    data = Data(config.the['file'])
    show(data.sway(), "mid", data.cols.y, 1)