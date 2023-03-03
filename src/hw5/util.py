import json
import math
import re
from copy import deepcopy
from string_util import *
import config as config
from lists import Lists

def itself(x):
    return x

def transpose(t):
    u = []
    for i in range(0, len(t[1])):
        u.append([])
        for j in range(0, len(t)):
            u[i].append(t[j][i])
    return u 


def dofile(sFile):
    with open(sFile, 'r', encoding = 'utf-8') as f:
        content  = f.read()
        content = re.findall(r'(return\s+[^.]+)', content)[0]
        map = {'return ' : '', '{' : '[', '}' : ']','=':':', '[\n':'{\n', '\n]':'\n}', '_':'"_"', '\'':'"'}
        for k,v in map.items():
            content = content.replace(k, v)
        content = re.sub("(\w+):",r'"\1":',content)
        parsed_json = json.loads(content)
        return parsed_json

def repPlace(data):
    n,g = 20,{}
    for i in range(1, n+1):
        g[i]={}
        for j in range(1, n+1):
            g[i][j]=' '
    maxy = 0
    print('')
    for r,row in enumerate(data.rows):
        c = chr(97+r).upper()
        print(c, row.cells[-1])
        x,y= row.x*n//1, row.y*n//1
        maxy = int(max(maxy,y+1))
        g[y+1][x+1] = c
    print('')
    for y in range(1,maxy+1):
        print(' '.join(g[y].values()))


def last(t):
    return t[-1]

def rint(lo,hi):
    return math.floor(0.5 + rand(lo, hi))

def any(t):
    return t[rint(0, len(t))-1]

def rnd(n, nPlaces = 3):
    mult = 10**nPlaces
    return math.floor(n * mult + 0.5) / mult

def rand(lo=0, hi=1):
        seed = (16807 * config.Seed) % 2147483647
        return lo + (hi - lo) * seed / 2147483647
def many(t,n):
    u=[]
    for _ in range(1,n+1):
        u.append(any(t))
    return u
def cliffsDelta(ns1,ns2):
    if len(ns1) > 256:
        ns1 = many(ns1,256)
    if len(ns2) > 256:
        ns2 = many(ns2,256)
    if len(ns1) > 10*len(ns2):
        ns1 = many(ns1,10*len(ns2))
    if len(ns2) > 10*len(ns1):
        ns2 = many(ns2,10*len(ns1))
    n,gt,lt = 0,0,0
    for x in ns1:
        for y in ns2:
            n = n + 1
            if x > y:
                gt = gt + 1
            if x < y:
                lt = lt + 1
    return abs(lt - gt)/n > config.the['cliffs']

def diffs(nums1, nums2):
    def helper(k, nums):
        return cliffsDelta(nums.has(), nums2[k].has()), nums.txt

    return Lists.kap(nums1, helper)

def value(has,nB = None, nR = None, sGoal = None):
    sGoal,nB,nR = sGoal or True, nB or 1, nR or 1
    b,r = 0,0
    for x,n in has.items():
        if x==sGoal:
            b = b + n
        else:
            r = r + n
    b,r = b/(nB+1/float("inf")), r/(nR+1/float("inf"))
    return b**2/(b+r)