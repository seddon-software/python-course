'''
Classes
=======
Here is a valid program with a user defined class.  The main point of interest is the Point constructor:
            def __init__(self, x0:int, y0:int) -> None:

1. You need to specify the return type of "__init__()" as None or the static analysis will report errors.  
2. Do not anotate "self"

Note too, that although @staticmethod is not required for static methods in Python3, mypy reports an error
if is missing for class methods not taking any parameters (but note __add__ has parameters and mypy doesn't 
report an error).
'''

############################################################
# 1) run the program
############################################################
from __future__ import annotations      # require for forward reference (Point)

class Point:
    count: int = 0

    def __init__(self:Point, x0:int=0, y0:int=0) -> None:
        Point.count += 1
        self.x = x0
        self.y = y0

    @staticmethod        # required by mypy
    def getCount()->int:
        return Point.count

    def moveBy(self:Point, dx:int, dy:int) -> None:
        self.x += dx
        self.y += dy

    def __add__(lhs:Point, rhs:Point) ->Point:
        result = Point()
        result.x = lhs.x + rhs.x
        result.y = lhs.y + rhs.y
        return result
            
p1 = Point(5, 9)
p2 = Point(4, 8)
p3 = p1 + p2

print(Point.getCount())

############################################################
# 2) perform static analysis with mypy
############################################################

import os
print(f"mypy {os.path.basename(__file__)}")
os.system(f"mypy {os.path.basename(__file__)}")
