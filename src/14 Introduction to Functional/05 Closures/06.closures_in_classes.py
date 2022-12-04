'''
Closures in Classes
===================

This time we form a closure using an object (p1 or p2) and a method (moveBy or zoom).  For example
        moveP1 = p1.moveBy

is a closure on the object p1 and method moveBy().  "moveP1" can now be passed as a parameter to another 
function (DoIt).  After all the partial functions have been called, the example concludes with printing the 
values of p1 and p2 to see the effect of the calls. 
'''

class Point:
    def __init__(self, x0, y0):
        self.x = x0
        self.y = y0
    
    def moveBy(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def zoom(self, xzoom, yzoom):
        self.x *= xzoom
        self.y *= yzoom
    
    def display(self):
        print((self.x, self.y))    
    
p1 = Point(5, 6)
p2 = Point(15, 16)

moveP1 = p1.moveBy      # closure on p1.x and p1.y
zoomP1 = p1.zoom        # closure on p1.x and p1.y
moveP2 = p2.moveBy      # closure on p2.x and p2.y
zoomP2 = p2.zoom        # closure on p2.x and p2.y

def DoIt(func, param1, param2):
    func(param1, param2)
    
DoIt(moveP1, 5, 1)
DoIt(moveP2, 6, 1)
DoIt(zoomP1, 10, 10)
DoIt(zoomP2, 20, 10)

p1.display()
p2.display()


