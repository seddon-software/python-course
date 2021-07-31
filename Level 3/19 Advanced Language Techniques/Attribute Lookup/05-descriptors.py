# the descriptor protocol defines 3 methods:
#    __get__()
#    __set__()
#    __delete__()
 
# any class implementing any of the above methods is a descriptor
# as in this class
class Trace(object):
    def __init__(self, name):
        self.name = name

    def __get__(self, obj, objtype):
        print(f"GET: {self.name} = {obj.__dict__[self.name]}")
        return obj.__dict__[self.name]

    def __set__(self, obj, value):
        obj.__dict__[self.name] = value
        print(f"SET: {self.name} = {obj.__dict__[self.name]}")


# define the class attributes to be references to instances of a descriptor
class Point(object):
# NOTES:
# 1. descriptor invoked by dotted attribute access:  A.x or a.x
# 2. descripor reference must be stored in the class dict, not the instance dict
# 3. descriptor not invoked by direct dictionary access: self.__dict__['x']

    x = Trace("x")
    y = Trace("y")
    
    def __init__(self, x0, y0):
        self.x = x0
        self.y = y0
    
    def moveBy(self, dx, dy):
        self.x = self.x + dx     # attribute access does trigger descriptor
        self.y = self.y + dy

# trace all getters and setters    
p1 = Point(15, 25)
p1.x = 20                   # uses descriptor protocol
p1.__dict__['x'] = 19       # this accesses the object dictionary directly
p1.y = 35
result = p1.x
p2 = Point(16, 26)
p2.x = 30
p2.moveBy(1, 1)

1






