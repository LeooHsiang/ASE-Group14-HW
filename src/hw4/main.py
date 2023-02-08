from test import show_settings, test_copy, test_every, test_nums, test_position, test_prototypes, test_repCols, test_repRows, test_syms, test_synonyms
from string_util import settings
from string_util import cli
from test import *
import config

def main(options, help, funs, saved = {}, fails = 0):
    """
    `main` fills in the settings, updates them from the command line, runs
    the start up actions (and before each run, it resets the random number seed and settongs);
    and, finally, returns the number of test crashed to the operating system.
    :param funs: list of actions to run
    :param saved: dictionary to store options
    :param fails: number of failed functions
    """
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
  
eg("the", "show settings", show_settings)
eg("copy", "check copy", test_copy)
eg("sym", "check syms", test_syms)
eg("num", "check nums", test_nums)
eg("repcols", "check repcols", test_repRows)
eg("synonyms", "check repcols cluster", test_synonyms)
eg("reprows","checking reprows", test_repCols)
eg('prototypes','checking reprows cluster', test_prototypes)
eg('position','where\'s wally', test_position)
eg('every','the whole enchilada', test_every)

main(config.the, config.help, egs)