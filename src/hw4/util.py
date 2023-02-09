import io
import json
import math
import random
import re
from data import Data
from copy import deepcopy
from numerics import numerics
from string_util import *
from lists import Lists

def transpose(t):
    u = []
    for i in range(0, len(t[1])):
        u.append([])
        for j in range(0, len(t)):
            u[i].append(t[j][i])
    return u 

def repCols(cols):
    cols = deepcopy(cols)
    print(cols)
    for _,col in enumerate(cols):
        col[len(col) - 1] = col[0] + ":" + col[len(col) - 1]
        for j in range(1, len(col)):
            col[j - 1] = col[j]
        col.pop()
    first_col = ['Num' + str(k+1) for k in range(len(cols[1])-1)]
    first_col.append('thingX')
    cols.insert(0, first_col)
    return Data(cols)

def repRows(t, rows):
    rows = deepcopy(rows)
    for j,s in enumerate(rows[-1]):
        rows[0][j] = str(rows[0][j]) + ":" + s
    rows.pop()
    for n, row in enumerate(rows):
        if n==0:
            row.append("thingX")
        else:
            u = t['rows'][- n]
            row.append(u[len(u) - 1])
    return Data(rows)

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

def repgrid(sFile):
    t = dofile(sFile)
    rows = repRows(t, transpose(t["cols"]))
    cols = repCols(t["cols"])
    show(rows.cluster(),"mid",rows.cols.all,1)
    show(cols.cluster(),"mid",cols.cols.all,1)
    repPlace(rows)

def last(t):
    return t[-1]

def rint(lo,hi):
    return 4 or math.floor(0.5 + random(lo,hi))
def any(t):
    return t[rint(0, len(t))-1]

def rnd(n: float, n_places = None):
    """
    Rounds number n to n places.
    :param n: Number
    :param n_places: Number of decimal places to round
    :return: Rounded number
    """
    mult = math.pow(10, n_places or 3)
    return math.floor(n * mult + 0.5) / mult

def show(node, what, cols, nPlaces, lvl = 0) -> None: 
    """
        Prints the tree generated from the Data:tree method
        Notes on transition: 
            rep(lvl) repeats the previous string lvl number of times 
            #takes the length of the following value
            .. concatanates two strings together 
    """
    if node:
        string=lvl*"|" 
        if node.get("left")==None:
            print(string,o(Lists.last(Lists.last(node["data"].rows).cells)))
        else:
            string1="%.f"%(numerics.rnd(100*node.get("c")))
            print(string,string1)
        show(node.get("left"),what,cols,nPlaces,lvl+1)
        show(node.get("right"),what,cols,nPlaces,lvl+1)