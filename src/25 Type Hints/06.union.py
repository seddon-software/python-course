'''
Union
=====
Union is used when a parameter can be multiple types.  Here number can be int or float.  Again, this is an 
invalid program that raises an exception and mypy reports what's wrong.  Note that the syntax for Union is 
changing to the more succinct form that uses | in later versions of Python
            number = int|float

instead of
            number = Union[int,float]

'''

############################################################
# 1) run the program
############################################################
from typing import Union

number = Union[int,float]           # use number = int|float from Python 3.10 onwards

def average(x:number, y:number, z:number) -> float:
    return (x + y + z)/3

try:
    print(average(1, 2, 3))
    print(average(10.1, 20.2, 30.3))
    print(average('A', 2, 3))
except Exception as e:
    print(e)

############################################################
# 2) perform static analysis with mypy
############################################################

import os
print(f"mypy {os.path.basename(__file__)}")
os.system(f"mypy {os.path.basename(__file__)}")
