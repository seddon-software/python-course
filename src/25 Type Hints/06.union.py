'''
Union
=====
Union is used when a parameter can be multiple types.  Here number can be int or float.  Again, this is an 
invalid program that raises an exception.  Mypy reports what's wrong.
'''

############################################################
# 1) run the program
############################################################
from typing import Union

number = Union[int,float]

def average(x:number, y:number, z:number) -> float:
    return (x + y + z)/3
# The following notation is simpler, but only available in Python 3.10
# def average(x: int|float, y: int|float, z: int|float) -> int|float:

try:
    print(average(1, 2, 3))
    print(average(10.1, 20.2, 30.3))
    print(average('A', 2, 3))
except Exception as e:
    print(e)

############################################################
# 2) perform static analysis with Mypy
############################################################

import os
print(f"mypy {os.path.basename(__file__)}")
os.system(f"mypy {os.path.basename(__file__)}")
