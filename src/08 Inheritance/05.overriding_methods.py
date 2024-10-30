import os; os.system("clear")
'''
  In this example we see how to add a "display" function to a derived class which prints out all
  the attributes of the class including the attributes defined in the base class.
 
  We need to arrange for the base class to return a string containing information about the base class 
  attributes and then append information about the derived class attributes.
	
  The best way to do this is to return f-strings from methods in both classes.

  Note how the derive class constructor calls the base class constructor.
'''

class Point:
    def __init__(self, x0, y0):
        self.x = x0
        self.y = y0
 
    def display(self):
        return f"x = {self.x}, y = {self.y}"

# derived classes can override methods (display)
class ColoredPoint(Point):
    def __init__(self, x0, y0, color): 
        Point.__init__(self, x0, y0)
        self.color = color
		
    def display(self):
	    return f"{Point.display(self)}, color: {self.color}"


def main():
    p = Point(5, 8)
    print(p.__dict__)
    
    cp = ColoredPoint(10, 20, "Blue")
    print(cp.__dict__)

    # now call the overriden method
    print(cp.display())


main()

