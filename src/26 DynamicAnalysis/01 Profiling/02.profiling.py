'''
This program uses cProfile to profile myprogram.foo(); it produces output in the binary file:
            stats/profilestats.out

The next example shows how to use this file to display results in a browser. 
'''

import os, pstats #, profilestats
import sys, cProfile

sys.path.append("src")
import myprogram


if not os.path.exists('stats'): os.mkdir('stats')
os.chdir('stats')
cProfile.run('myprogram.foo()', 'profilestats.out')


