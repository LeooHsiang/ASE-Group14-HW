from sym import Sym
from num import Num
from numerics import rand ,rint, rnd
def test_global_options() -> bool:
    return True

def test_rand() -> bool:
    num1 = Num()
    num2 = Num()
    for i in range(1000):
        num1.add(rand(937162211,0,1))
    for i in range(1000):
        num2.add(rand(937162211,0,1))
    m1= rnd(num1.mid(),10)
    m2= rnd(num2.mid(),10)
    return m1==m2 and .5 == rnd(m1,1)

def test_num() -> bool:
    num=Num()
    nums=[1,1,1,1,2,2,3]
    for i in nums:
        num.add(i)
    return 11/7 == num.mid() and 0.787 == rnd(num.div())
    

def test_sym() -> bool:
    sym=Sym()
    symbols=["a","a","a","a","b","b","c"]
    for s in symbols:
        sym.add(s)
    return ("a"==sym.mid() and 1.379 == rnd(sym.div()))