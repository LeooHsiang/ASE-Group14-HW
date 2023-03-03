from discretization import bins
from string_util import *
from util import *
import config as config
from lists import Lists
from data import Data
from num import Num
from sym import Sym
from col import Col

# This is the file that holds the functions for all of the tests


def show_settings():
    print(config.the)


def checkRand():
  # Checks to make sure the random generator is working
  s = config.Seed

  config.Seed = 1
  t = []
  for i in range(1,1000+1):
    t.append(rint(0,100))
  u=[]
  for i in range(1,1000+1):
    u.append(rint(0,100))
  for k,v in enumerate(t):
    assert(v==u[k])


def checkSome():
  # Checks to make sure we can grab some numbers correctly
  config.the["Max"] = 32
  num1 = Num()
  for i in range(1, 10001):
    num1.add(i)
    print(num1.has)


def checkNums():
  # Checks to make sure nums are created and added correctly
    num1 = Num()
    num2 = Num()
    for i in range(1,10**3+1):
        num1.add(rand(0,1))
    for i in range(1,10**3+1):
        num2.add(rand(0,1)**2)
    m1,m2 = rnd(num1.mid(),1), rnd(num2.mid(),1)
    d1,d2 = rnd(num1.div(),1), rnd(num2.div(),1)
    print(1, m1, d1)
    print(2, m2, d2)
    return m1 > m2 and .5 == rnd(m1,1)


def checkSyms():
  # Checks to make sure syms are created and added correctly
  sym = Sym()
  for x in ["a","a","a","a","b","b","c"]:
    sym.add(x)
  print(sym.mid(), rnd(sym.div()))
  return 1.379 == rnd(sym.div())


def no_of_chars_in_file(t):
    config.n += len(t)

def checkCsv():
  # Checks to make sure the data is read correctly
   n = 0
   csv(config.the['file'], no_of_chars_in_file)
   print(n)
   return n == 3192


def checkData():
  # Checks to make sure the data is created correctly
  data=Data(config.the['file'])
  col=data.cols.x[1]
  print(col.lo,col.hi, col.mid(),col.div())
  print(data.stats('mid', data.cols.y, 2))


def checkClone():
  # Checks to make sure the data can be cloned correctly
  data1=Data(config.the['file'])
  data2 = data1.clone(data1.rows)
  print(data1.stats('mid', data1.cols.y, 2))
  print(data2.stats('mid', data2.cols.y, 2))


def checkCliffs():
  # Checks to make sure cliffsDelta catagorizes correctly
  assert(False == cliffsDelta( [8,7,6,2,5,8,7,3],[8,7,6,2,5,8,7,3]))
  assert(True  == cliffsDelta( [8,7,6,2,5,8,7,3], [9,9,7,8,10,9,6]))
  t1,t2=[],[]
  for i in range(1,1000+1):
        t1.append(rand(0,1))
  for i in range(1,1000+1):
        t2.append(rand(0,1)**.5)
  assert(False == cliffsDelta(t1,t1))
  assert(True  == cliffsDelta(t1,t2))
  diff,j=False,1.0
  while not diff:
        def function(x):
            return x*j
        t3=list(map(function, t1))
        diff=cliffsDelta(t1,t3)
        print(">",rnd(j),diff)
        j=j*1.025


def checkDist():
  # Checks to make sure the distance funciton works properly
    data = Data(config.the['file'])
    num  = Num()
    for row in data.rows:
        num.add(data.dist(row, data.rows[1]))
    print({'lo' : num.lo, 'hi' : num.hi, 'mid' : rnd(num.mid()), 'div' : rnd(num.div())})


def checkHalf():
  # Checks to make sure that the data can be split in half correctly
  data = dofile(config.the["file"])
  left, right, A, B, c = Num.half(data)
  print(len(left), len(right))
  l = deepcopy(data, left)
  r = deepcopy(data, right)
  print("l", Data.stats(l)[0])
  print("r", Data.stats(r)[0])
 

def checkTree():
  # Checks to make sure trees are made correctly
  Data.showTree(Data.tree(dofile(config.the["file"])))

def checkHalf():
    data=Data(config.the['file'])
    left,right,A,B,mid,c = data.half() 
    print(len(left),len(right),len(data.rows))
    print(A.cells,c)
    print(mid.cells)
    print(B.cells)
    
def checkSway():
  # Checks to make sure the sway function works properly
  data = dofile(config.the["file"])
  best, rest = Data.sway(data)
  print("\nall ", Data.stats(data)[0]) 
  print("    ",   Data.stats(data,Num.div)[0]) 
  print("\nbest", Data.stats(best)[0]) 
  print("    ",   Data.stats(best,Num.div)[0]) 
  print("\nrest", Data.stats(rest)[0]) 
  print("    ",   Data.stats(rest,Num.div)[0]) 
  print("\nall ~= best?", diffs(best["cols"]["y"], data["cols"]["y"]))
  print("best ~= rest?", diffs(best["cols"]["y"], rest["cols"]["y"]))

def checkClone():
    data1 = Data(config.the["file"])
    data2 = data1.clone(data1.rows)

    return (
        len(data1.rows) == len(data2.rows)
        and data1.cols.y[1].w == data2.cols.y[1].w
        and data1.cols.x[1].at == data2.cols.x[1].at
        and len(data1.cols.x) == len(data2.cols.x)
    )

def checkBins():
  # Checks to make sure the bins works correctly
    b4 = ""
    data = Data(config.the['file'])
    best,rest = data.sway()
    print("all","","","",{'best':len(best.rows), 'rest':len(rest.rows)})
    for k,t in enumerate(bins(data.cols.x,{'best':best.rows, 'rest':rest.rows})):
        for range in t:
            if range['txt'] != b4:
                print("")
            b4 = range['txt']
            print(range['txt'],range['lo'],range['hi'],
            rnd(value(range['y'].has, len(best.rows),len(rest.rows),"best")),
            range['y'].has)