############################################################
#
#    Undo
#
############################################################

import math
from copy import copy

class Point(object):
    history = dict()
    
    def __init__(self, x0 = 0, y0 = 0): 
        self.x = x0
        self.y = y0
        self.distance = 0
        Point.history[id(self)] = [copy(self)]
                    
    def MoveBy(self, dx, dy):        
        history = Point.history[id(self)]
        old = history[-1]
        self.x += dx;
        self.y += dy;
        self.distance += self.Distance(old)
        history.append(copy(self))
        Point.history[id(self)] = history
        
    def Print(self):
        print(str(id(self)) + ":", end=' ')
        print("x =%3i," % self.x, end=' ')
        print("y =%3i" % self.y, end=' ')
        print("distance =" + ("%6.2f" % self.distance))
    
    def Undo(self):
        history = Point.history[id(self)]
        history.pop()
        p = history[-1]
        self.x = p.x
        self.y = p.y
        self.distance = p.distance
        Point.history[id(self)] = history
    
    def Distance(self, rhs):
        dx = self.x - rhs.x
        dy = self.y - rhs.y
        return math.sqrt(dx * dx + dy * dy)

############################################################

p = Point(27, 31); p.Print()
q = Point(5, 5); q.Print()

p.MoveBy(10, 20); p.Print()
p.MoveBy(10, 20); p.Print()
p.MoveBy(10, 20); p.Print()
p.Undo(); p.Print()

q.MoveBy(1,1); q.Print()
q.Undo(); q.Print()

p.MoveBy(10, 20); p.Print()
p.Undo(); p.Print()
p.Undo(); p.Print()
p.Undo(); p.Print()

