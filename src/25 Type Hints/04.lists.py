'''
Lists
=====
This example is valid, so Mypy should report all is well
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
# 2) perform static analysis with Mypy
############################################################
import os
print(f"mypy {os.path.basename(__file__)}")
os.system(f"mypy {os.path.basename(__file__)}")

