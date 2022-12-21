'''
Classes
=======
Here is a valid program with a user defined class.  The main point of interest is the Point constructor:
            def __init__(self, x0:int, y0:int) -> None:

You need to specify the return type of "__init__()" as None or the static analysis will report errors.

Note too, that @staticmethod is not required for static methods in Python3.  However, mypy reports an error
if you don't use @staticmethod.
'''

############################################################
# 1) run the program
############################################################

class Point:
    count: int = 0

    def __init__(self, x0:int, y0:int) -> None:
        Point.count += 1
        self.x = x0
        self.y = y0

    @staticmethod        # required by mypy
    def getCount()->int:
        return Point.count


p1 = Point(5, 9)
p2 = Point(4, 8)
p3 = Point(3, 7)

print(Point.getCount())

############################################################
# 2) perform static analysis with mypy
############################################################

import os
print(f"mypy {os.path.basename(__file__)}")
os.system(f"mypy {os.path.basename(__file__)}")
