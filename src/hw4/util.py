import io
import math
import re
from num import NUM
from sym import SYM
from data import DATA
from math import floor
from copy import deepcopy
import string_util

def transpose(t):
    u = []
    for i in range(0, len(t[0])):
        u.append([])
        for j in range(0, len(t)):
            u[i].append(t[j][i])
    return u 

def repCols(cols):
    cols = deepcopy(cols)
    for _,col in enumerate(cols):
        col[len(col)] = str(col[0]) + ":" + str(len(col))
        for j in range(1, len(col)):
            col[j - 1] = col[j]
        col.pop()
    cols.insert(0, ['Num' + str(k) for k in range(len(cols[0]))])
    cols[0][-1] = "thingX"
    return DATA(cols)

def repRows(t, rows, u):
    rows = deepcopy(rows)
    for j,s in enumerate(rows[-1]):
        rows[0][j] = str(rows[0][j]) + ":" + str(s)
    rows.pop()
    for n, row in enumerate(rows):
        if n==0:
            row.append("thingX")
        else:
            u = t["rows"][len(t["rows"]) - n + 2]
            row.append(u[-1])
    return DATA(rows)

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

def repgrid(sFile):
    t = dofile(sFile)
    rows = repRows(t, transpose(t["cols"]))
    cols = repCols(t["cols"])
    show(rows.cluster())
    show(cols.cluster())
    repPlace(rows)


def show(node, what, cols, nPlaces, lvl = 0) -> None: 
    """
        Prints the tree generated from the Data:tree method
        Notes on transition: 
            rep(lvl) repeats the previous string lvl number of times 
            #takes the length of the following value
            .. concatanates two strings together 
    """
    if node:
        lvl = lvl or 0
        print("|.. " * lvl, end="")
        if ("left" not in node):
            print(last(last(node.data.rows).cells))
        else:
            print(str(int(100 * node["C"])))

        show(node.get('left',None), what, cols, nPlaces, lvl + 1)
        show(node.get('right',None), what, cols, nPlaces, lvl + 1)

