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

def settings(s, t):
    t = {}
    s = re.compile("\n[%s]+[-][%S]+[%s]+[-][-]([%S]+)[^\n]+= ([%S]+)")
    for match in s.finditer(help):
        k, v = match.group(1, 2)
        t[k] = s.coerce(v)
    return t

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

def main(options, help, funs, k, saved, fails):
    saved,fails={}, 0
    for k, v in cli(settings(help)).items():
        options[k] = v
        saved[k] = v
    
    if options.help:
        print(help)
    
    else:
        for what, fun in funs.items():
            if options.go == "all" or what == options.go:
                for k,v in saved.items():
                    options[k] = v
                Seed = options.seed
                if funs[what] == 'false':
                    fails = fails + 1
                    print("❌ fail:", what)
                else:
                    print("✅ pass:", what)


    # for k,v in pairs(_ENV) do 
    # if not b4[k] then print( fmt("#W ?%s %s",k,type(v)) ) end end 
    # os.exit(fails) end 