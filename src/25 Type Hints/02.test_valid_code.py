'''
Test Valid Code
===============
Here is a valid program that uses type hints.  The Python interpreter ignores these hints at run-time, but you can 
use Mypy to perform a check that the program is indeed valid.

We run this example first and then do a static analysis with mypy.  Note that the third parameter is 9, which is an 
int - this gets converted automatically to a float and hence passes the static analysis check.
'''

############################################################
# 1) run the program
############################################################
def average(x:float, y:float, z:float) -> float:
    return (x + y + z)/3.0

print(average(5.5, 7.7, 9))

############################################################
# 2) perform static analysis with mypy
############################################################
import os
print(f"mypy {os.path.basename(__file__)}")
os.system(f"mypy {os.path.basename(__file__)}")
