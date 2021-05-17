import sys, os, pstats, profilestats

sys.path.append("src")
import myprogram


if not os.path.exists('stats'): os.mkdir('stats')
os.chdir('stats')

# this decorator profiles individual functions and creates two files in stats directory: 
#    callgrind.out (in KCachegrind-compatible format)
#    profilestats.out (in cProfile format)

@profilestats.profile(print_stats=0, dump_stats=True)
def profileIt():
    myprogram.foo()

def reportUsingStats():
#     stats = pstats.Stats('profilestats.prof')
    stats = pstats.Stats('profilestats.out')
    stats.strip_dirs()
    stats.sort_stats('cumulative')
    stats.print_stats()


def reportUsingKCachegrind():
    # need to install KCacheGrind program (not a Python module and only runs on Unix)
    pass

profileIt()
reportUsingStats()
reportUsingKCachegrind()

