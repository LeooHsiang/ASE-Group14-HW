import math

global the, Help, Seed

the,help = {},"""
gird.lua : a rep grid processor
(c)2022, Tim Menzies <timm@ieee.org>, BSD-2 
USAGE: grid.lua  [OPTIONS] [-g ACTION]
OPTIONS:
  -d  --dump    on crash, dump stack   = false
  -f  --file    name of file           = etc/data/repgrid1.csv
  -g  --go      start-up action        = data
  -h  --help    show help              = false
  -p  --p       distance coefficient   = 2
  -s  --seed    random number seed     = 937162211
ACTIONS:
"""
    
Seed = 927162211

def rint(nlo, nhi): 
  return math.floor(.5 + rand(nlo, nhi))

def rand(nlo, nhi): 
  nlo = nlo if nlo is not None else 0 
  nhi = nhi if nhi is not None else 1 
  seed = (16807 * Seed) % 2147483647
  return nlo + (nhi - nlo) * seed / 2147483647