from sym import Sym
from num import Num
from numerics import numerics
from strings import strings
from config import *

def eg(key,string,fun):
  global egs, Help
  egs[key]=fun
  Help = Help + ("  -g  %s\t%s\n" % (key,string))

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

def test_the():
    return (the.__repr__())


def test_rand():
    num1, num2 = Num(), Num()
    global Seed
    Seed = the['seed']
    for i in range(1,10**3+1):
        num1.add(numerics.rand(0,1))
    Seed = the['seed']
    for i in range(1,10**3+1):
        num2.add(numerics.rand(0,1))
    m1,m2 = numerics.rnd(num1.mid(),1), numerics.rnd(num2.mid(),1)
    return m1==m2 and .5 == numerics.rnd(m1,1)

if __name__ == "__main__":
    print(test_sym())
    print(test_num())
    print(test_the())
    print(test_rand())