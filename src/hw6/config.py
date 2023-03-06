import math


the,help = {},"""
bins: multi-objective semi-supervised discetization
(c) 2023 Tim Menzies <timm@ieee.org> BSD-2
  
USAGE: lua bins.lua [OPTIONS] [-g ACTIONS]
  
OPTIONS:
  -b  --bins    initial number of bins       = 16
  -c  --cliffs  cliff's delta threshold      = .147
  -f  --file    data file                    = etc/data/auto93.csv
  -F  --Far     distance to distant          = .95
  -g  --go      start-up action              = nothing
  -h  --help    show help                    = false
  -H  --Halves  search space for clustering  = 512
  -m  --min     size of smallest cluster     = .5
  -M  --Max     numbers                      = 512
  -p  --p       dist coefficient             = 2
  -r  --rest    how many of rest to sample   = 4
  -R  --Reuse   child splits reuse a parent pole = true
  -s  --seed    random number seed           = 937162211
"""
    
Seed = 937162211

n = 0

def rint(nlo, nhi): 
  return math.floor(.5 + rand(nlo, nhi))

def rand(nlo, nhi): 
  nlo = nlo if nlo is not None else 0 
  nhi = nhi if nhi is not None else 1 
  seed = (16807 * Seed) % 2147483647
  return nlo + (nhi - nlo) * seed / 2147483647

def rnd(n, nPlaces=3):
    mult=10**(nPlaces or 3)
    return math.floor(n*mult + 0.5)/mult