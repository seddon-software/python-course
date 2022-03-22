'''
Test Valid Code
===============
Here is a valid program that uses type hints.  The Python interpreter ignores these hints at run-time, but you can 
use Mypy to check the program is indeed valid.

We run this example first and then do a static analysis with Mypy.
'''

############################################################
# 1) run the program
############################################################
def average(x:float, y:float, z:float) -> float:
    return (x + y + z)/3.0

print(average(5.5, 7.7, 9))

############################################################
# 2) perform static analysis with Mypy
############################################################
import os
print(f"mypy {os.path.basename(__file__)}")
os.system(f"mypy {os.path.basename(__file__)}")
