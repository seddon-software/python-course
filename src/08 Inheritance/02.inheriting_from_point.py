import os; os.system("clear")
'''
Inheritance
===========

One class can inherit from another as in:
            class ColoredPoint(Point):

The inheriting class is usually called the derived class (ColoredPoint) and inherits all method from 
it's base class (Point) except the constructor (__init__):
            def __init__(self, x, y):
            def whereAmI(self):
            def moveBy(self, dx, dy):

and can define additional methods:
            def changeColor(self, newColor)
            def display(self)

Although the derived class inherits the __init__() method from it's base class, it makes sense to provide
it's own constructor so that is can initialise any additional fields defined in the derived class.  In the new
constructor, we call the base constructor to initilize the fields defined in the base class:
            def __init__(self, x, y, color):
                Point.__init__(self, x, y)
                self.color = color

Although the x and y attributes are defined in the base class, they end up the derived object's dictionary, 
as verified by:
            print( cp.__dict__ )

However the really interesting part of the code is when we call the function:
            def WhereAreYou(p)

This function is not part of either class.  Now, because both the base class and derived class share methods,
when calling this function you can pass a base or a derived object, provided the function only ever calls
base class methods.  This is an example of the substitution rule:  a function only call base class methods
can be called by a base object or any object that can substitute for the base object (i.e. with identical
methods).  Obviously, a derived object can substitute for a base object for such functions. 

Note the convention of defining classes starting with an upper case letter and methods with a lower case
letter.

'''

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def whereAmI(self):
        print(f"Point({id(self)}) is at {self.x},{self.y}")

    def moveBy(self, dx, dy):
        self.x += dx
        self.y += dy

class ColoredPoint(Point):
    def __init__(self, x, y, color):
        Point.__init__(self, x, y)
        self.color = color
        
    def changeColor(self, newColor):
        self.color = newColor
    
    def display(self):
        self.whereAmI()
        print(" ... and color is %s" % self.color)
        

# this function supports the substitution rule
def WhereAreYou(p):  # p can be instance of Point or ColoredPoint
                     # ... the substitution rule
    p.whereAmI()

# define a base object and a derived object
p = Point(5,8)
cp = ColoredPoint(15,25,"Blue")

# inspect derived object's dictionary
print( cp.__dict__ )

# call methods
p.whereAmI()
cp.whereAmI()       # inherited method
cp.display()

cp.changeColor("Cyan")
cp.moveBy(5,15)     # inherited method
cp.display()

# use substitution rule
WhereAreYou(p)
WhereAreYou(cp)
