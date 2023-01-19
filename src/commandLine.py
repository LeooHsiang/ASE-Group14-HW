import sys
import re
from strings import strings as s

'''Defines command line arguments'''

#default values
help = "USAGE: py helper.py [OPTIONS] [-g ACTION]\n\n\
-d --dump   on crash, dump stack = false\n\
-g --go    start-up action = data\n\
-h --help   show help   = false\n\
-s --seed   random number seed  = 937162211"

arg = sys.argv[1:]

the = {}
pattern = re.compile("\n[%s]+[-][%S]+[%s]+[-][-]([%S]+)[^\n]+= ([%S]+)")
for match in pattern.finditer(help):
    k, v = match.group(1, 2)
    the[k] = s.coerce(v)

#check if int and convert to string
def coerce(s):
    return int(s) if s.isdigit() else s

"""
Reads in default options and stores in configuration dictionary "the"
t = dictionary of options
"""
def cli(options):
    for k, v in options.items():
        v = str(v)
        for n, x in enumerate(arg):
            if x == "-" + k[0] or x == "--" + k:
                v = v == "false" and "true" or v == "true" and "false" or arg[n + 1]
        options[k] = s.coerce(v)
    return options     

the = cli(the)
