import sys, os, pstats #, profilestats
import sys, myprogram, cProfile

sys.path.append("src")
import myprogram


if not os.path.exists('stats'): os.mkdir('stats')
os.chdir('stats')
cProfile.run('myprogram.foo()', 'profilestats.out')


