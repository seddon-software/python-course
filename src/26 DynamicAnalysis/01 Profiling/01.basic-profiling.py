import sys, cProfile
sys.path.append("src")
import myprogram 
cProfile.run('myprogram.foo()')

