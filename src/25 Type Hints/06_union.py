############################################################
#
#       Type hints: Union
#
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

#):
############################################################
# now check the above code
############################################################

import os
print(f"mypy {os.path.basename(__file__)}")
os.system(f"mypy {os.path.basename(__file__)}")
