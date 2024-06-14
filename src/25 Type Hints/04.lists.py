'''
Lists
=====
This example is valid, so mypy should report all is well.  This shows how to add type hints for lists of int.  Note
the use of a type alias:
            IntArray = list[int]

or alternatively:
            IntArray: TypeAlias = list[int] 

and from Python 3.12 onwards you should use the slightly more informative form:
            type IntArray = list[int]
'''

############################################################
# 1) run the program
############################################################

def average1(nums: list[int]) -> float:
    total = sum(nums)
    count = len(nums)
    return total / count

# alternative version using a type alias

IntArray = list[int] # Python < 3.12
# type IntArray = List[int] # Python >= 3.12
def average2(nums: IntArray) -> float:
    total = sum(nums)
    count = len(nums)
    return total / count

print(average1([1, 2, 3, 4]))
print(average2([1, 2, 3, 4]))

############################################################
# 2) perform static analysis with mypy
############################################################
import os
print(f"mypy {os.path.basename(__file__)}")
os.system(f"mypy {os.path.basename(__file__)}")

