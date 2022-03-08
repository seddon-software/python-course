from collections import namedtuple
from collections import Sequence

def moveBy(self, dx, dy):
    self.x += dx
    self.y += dy

Point = namedtuple("Point", ['x', 'y'])
p = Point(4, 5)
Point.moveBy = moveBy

print(p)
p.moveBy(10, 10)


