'''
Lists
=====
This example is valid, so mypy should report all is well.  This show how to add type hints for lists of int.
'''

############################################################
# 1) run the program
############################################################
from typing import List

def average(nums: List[int]) -> float:
    total = sum(nums)
    count = len(nums)
    return total / count

print(average([1, 2, 3, 4]))

############################################################
# 2) perform static analysis with mypy
############################################################
import os
print(f"mypy {os.path.basename(__file__)}")
os.system(f"mypy {os.path.basename(__file__)}")

