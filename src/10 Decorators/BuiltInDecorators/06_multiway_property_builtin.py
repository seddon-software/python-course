############################################################
#
#    property built in
#
############################################################

# define a class where methods are invoked through properties
class Point(object):
    def getX(self):
        print("getting x")
        return self._x

    def setX(self, value):
        print("setting x")
        self._x = value

    def delX(self):
        print("deleting x")
        del self._x

    x = property(getX, setX, delX)

p = Point()
p.x = 55    # calls setX
a = p.x     # calls getX
#del p.x     # calls delX
print(Point.__dict__)
print(p.__dict__)

# using property decorator (read only attributes)
class Foo(object):
    def __init__(self, x0, y0):
        self.__dict__["myX"] = x0
        self.__dict__["myY"] = y0
        
    @property
    def x(self):
        return self.myX
        
f = Foo(4,6)
print(f.x)
try:
    f.x = 77        # fails: f.x is read-only
except Exception as e:
    print(e)


    

