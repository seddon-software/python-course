from typing import Union

# only available in Python 3.10
# def average(x: int|float, y: int|float, z: int|float) -> int|float:

number = Union[int,float]
def average(x:number, y:number, z:number) -> float:
    return (x + y + z)/3

try:
    print(average(1, 2, 3))
    print(average(10.1, 20.2, 30.3))
    print(average('A', 2, 3))
except Exception as e:
    print(e)

import os
os.system("mypy 06_casting.py")
