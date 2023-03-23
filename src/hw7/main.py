from test import sk_test, tiles_test, six_test, five_test, pre_test, basic_test, bootmu_test, gauss_test, num_test, sample_test, ok_test  
import config
from string_util import settings
from string_util import cli
from test import *



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
  
eg("ok", "seed generation", ok_test)
eg("sample", "demo of samples", sample_test)
eg("nums","demo of NUM", num_test)
eg("gauss", "demo of gaussian", gauss_test)
eg("boot", "demo of boot", bootmu_test)
eg("basic", "demo of basic", basic_test)
eg("pre", "demo of pre", pre_test)
eg("five", "demo for five", five_test)
eg("tiles", "check tiles", tiles_test)
eg("sk", "check sk", sk_test)
eg("six", "demo for six", six_test)

main(config.the, config.help, egs)