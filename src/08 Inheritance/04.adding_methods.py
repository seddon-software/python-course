'''
  An alternative way of looking at the SUBSTITUTE rule is to say a derived class object IS A kind of base 
  class object.

  In this example we define a base class Point and two derived classes.  All derived classes support the
  ISA relationship:
            Snap ISA Point
            ColouredPoint ISA Point
 
  The Snap class needs to access its x and y attributes in order to snap to the grid.  The class also needs
  to override the MoveBy method in order to ensure its new position is still on the grid.
 
  The ColordPoint class adds the method:
            changeColor()
  to support its additional attribute: color
 
  Note: the display() method from the previous example with __str__() to simplify printing objcts.
'''

# this is the base class
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # this overload is invoked by derived classes and works because of the SUBSTUTION RULE (Point&).
    def __str__(self):
        return f"x = {self.x}, y = {self.y}"
    
    def moveBy(self, dx, dy):
        self.x += dx
        self.y += dy


class Snap(Point):
    # the x and y coords must be a multiple of 10 to snap to a grid of spacing of 10 units
    # the x and y attributes should be initialized by the base class
    def __init__(self, x=0, y=0): 
        Point.__init__(self, x-x%10, y-y%10)
        
    # we need to override the base class method in order to ensure snapping to grid
    def moveBy(self, dx, dy):
        Point.moveBy(self, dx, dy)
        self.x -= self.x%10
        self.y -= self.y%10

    def __str__(self):
        return f"{Point.__str__(self)}"

class ColoredPoint(Point):
    def __init__(self, x, y, color): 
        Point.__init__(self, x,y)
        self.color = color

    def changeColor(self, newColor):
        self.color = newColor

    def __str__(self):
        return f"{Point.__str__(self)}, Color: {self.color}"

def main():
    point = Point(53, 18)
    print(point)

    snap = Snap(13, 27)
    print(snap)

    snap.moveBy(29, 17)
    print(snap)

    colored = ColoredPoint(15, 18, "red")
    print(colored)
    colored.changeColor("blue")
    print(colored)

main()
