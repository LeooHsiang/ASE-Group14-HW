from sym import Sym
from num import Num
from numerics import numerics
from string_util import *
import config as config

def oo(t):
  print(t)

def test_sym():
    sym=Sym()
    symbols=["a","a","a","a","b","b","c"]
    for s in symbols:
        sym.add(s)
    return ("a"==sym.mid() and 1.379 == numerics.rnd(sym.div()))

def test_num():
    num=Num()
    nums=[1,1,1,1,2,2,3]
    for i in nums:
        num.add(i)
    return 11/7 == num.mid() and 0.787 == numerics.rnd(num.div())


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
