import io
import json
import re
from data import Data
from copy import deepcopy
from numerics import numerics
from string_util import *

def transpose(t):
    u = []
    for i in range(0, len(t[1])):
        u.append([])
        for j in range(0, len(t)):
            u[i].append(t[j][i])
    return u 

def repCols(cols, Data):
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

def repRows(t, Data, rows):
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
    file = open(sFile, 'r', encoding='utf-8')
    text  = re.findall(r'(?<=return )[^.]*', file.read())[0].replace('{', '[').replace('}',']').replace('=',':').replace('[\n','{\n' ).replace(' ]',' }' ).replace('\'', '"').replace('_', '"_"')
    file.close()
    return json.loads(re.sub("(\w+):", r'"\1":', text))

def repPlace(data):
    n,g = 20,[]
    for i in range(n+1):
        g.append([])
        for j in range(n+1):
            g[i].append(" ")
    maxy = 0
    print("")
    for r, row in enumerate(data.rows):
        c = chr(r+65)
        print(c, last(row.cells))
        x, y = int(row.x*n), int(row.y*n)
        maxy = max(maxy, y)
        g[y][x] = c
    print("")
    for y in range(maxy):
        oo(g[y])

def repgrid(sFile, Data):
    t = dofile(sFile)
    rows = repRows(t, Data, transpose(t["cols"]))
    cols = repCols(t["cols"], Data)
    show(rows.cluster(),"mid",rows.cols.all,1)
    show(cols.cluster(),"mid",cols.cols.all,1)
    repPlace(rows)

def last(t):
    return t[-1]

def show(node, what, cols, nPlaces, lvl = 0) -> None: 
    """
        Prints the tree generated from the Data:tree method
        Notes on transition: 
            rep(lvl) repeats the previous string lvl number of times 
            #takes the length of the following value
            .. concatanates two strings together 
    """
    if node:
        print(
            f"{'| ' * lvl}"
            f"{len(node['data'].rows)}  "
            f"{node['data'].stats(node['data'].cols.y, nPlaces, 'mid') if 'left' not in node or lvl == 0 else ''}"
        )

        show(node.get('left',None), what, cols, nPlaces, lvl + 1)
        show(node.get('right',None), what, cols, nPlaces, lvl + 1)

