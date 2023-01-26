from test import test_rand, test_read_csv, test_read_data_csv, test_stats_data
from test import show_settings, test_nums, test_syms
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

eg("rand", "generate, reset, regenerate same", test_rand)

eg("sym", "check syms", test_syms)

eg("num", "check nums", test_nums)

eg("csv","read from csv", test_read_csv)
eg("data","read DATA csv", test_read_data_csv)
# eg("stats","stats from DATA", test_stats_data)

main(config.the, config.help, egs)