from test import oo
from test import test_num
from test import test_sym
from test import test_rand
from string_util import settings
from string_util import cli
from test import *
import config

def main(options, help, funs, saved = {}, fails = 0):
    
    for k, v in cli(settings(help)).items():
        options[k] = v
        saved[k] = v

    if options["help"]:
        print(help)
    else:
        for what in funs:
            if options["go"] == "all" or what == options["go"]:
                for k,v in saved.items():
                    options[k] = v
                if funs[what]() == False:
                    fails = fails + 1
                    print("❌ fail:", what)
                else:
                    print("✅ pass:", what)
    exit(fails)
    
egs = {}
def eg(key,string,fun):
  global egs
  egs[key]=fun
  config.help = config.help + ("  -g  %s\t%s\n" % (key,string))
  
eg("the", "show settings", lambda: oo(config.the))

eg("rand", "generate, reset, regenerate same", test_rand)

eg("sym", "check syms", test_sym)

eg("num", "check nums", test_num)

main(config.the, config.help, egs)

    # for k,v in pairs(_ENV) do 
    # if not b4[k] then print( fmt("#W ?%s %s",k,type(v)) ) end end 
    # os.exit(fails) end 