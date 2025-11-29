'''
Property built-in Function
==========================
The property built in function is used by the decorators we have just looked at.  This built in function
traps attribute access and redirects the appropriate getter, setter or deleter method you define in:
            x = property(getX, setX, delX)
            y = property(getY, setY, delY)

where x and y are defined as class attributes and not object attributes.

Note that in this example, we bypass the property function in the Point constructor by accessing the
object dictionary directly as in:
            self.__dict__["_x"] = x0
            self.__dict__["_y"] = y0

Note the lines:
            print(p.__dict__) 
            print(Point.__dict__) 

These demonstrate that the object attributes are "_x" and "_y" and that "x" and "y" are class attributes.
The code gives the illusion that the object has attributes "x" and "y".
'''

# define a class where methods are invoked through properties
class Point:
    def getX(self):
        print("getting x")
        return self._x

    def setX(self, value):
        print(f"setting x = {value}")
        self._x = value

    def delX(self):
        print("deleting x")
        del self._x

    def getY(self):
        print("getting y")
        return self._y

    def setY(self, value):
        print(f"setting y = {value}")
        self._y = value

    def delY(self):
        print("deleting y")
        del self._y

    # CTOR bypasses the property function by accessing dictionary directly
    def __init__(self, x0, y0):
        self.__dict__["_x"] = x0
        self.__dict__["_y"] = y0

    # define class attributes to shadow attribute access
    x = property(getX, setX, delX)
    y = property(getY, setY, delY)

# call the CTOR
p = Point(4, 6)

# look at object and class dictionaries
print(p.__dict__) 
print(Point.__dict__) 
    
# access "virtual" attributes "x" and "y" 
print(f"p.x = {p.x}")     # calls getX
print(f"p.y = {p.y}")     # calls getY
p.x = 44    # calls setX
p.y = 66    # calls setY
del p.x     # calls delX
del p.y     # calls delY

# look at object dictionary to see the effect of del
print(f"object dictionary is: {p.__dict__}")


    

