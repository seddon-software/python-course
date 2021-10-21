############################################################
#
#       Type hints: List
#
############################################################

from typing import List

def average(nums: List[int]) -> float:
    total = sum(nums)
    count = len(nums)
    return total / count

print(average([1, 2, 3, 4]))

#):
############################################################
# now check the above code
############################################################

import os
print(f"mypy {os.path.basename(__file__)}")
os.system(f"mypy {os.path.basename(__file__)}")

