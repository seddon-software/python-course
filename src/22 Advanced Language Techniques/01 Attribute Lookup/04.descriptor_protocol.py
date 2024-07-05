'''
Descriptor Protocol
===================
The descriptor protocol allows you to intercept all dotted object attribute lookups.  The protocol defines 3 
methods:
            __get__()
            __set__()
            __delete__()
 
In this example we define a descriptor class called "Trace" that implements the __get__() and __set()__ descriptor
methods.  This class is used to intercept lookups on another class, namely "Point".

Any class ("Trace") implementing any of the above methods is defined as a descriptor class.  Objects of the 
descriptor class intercept dotted attribute access on a separate class ("Point").  Effectively they allow you 
to override the dot operator in the other class, for example:
            result = p1.x           calls Trace.__get__()
            p1.x = 20               calls Trace.__set__()


Note, for the descriptor to become active you must define class attributes in the "Point" class with the same 
names as the object attributes being intercepted, in this case x and y:
            x = Trace("x")
            y = Trace("y")

Note:
    1) the descriptor is invoked by dotted attribute access:  A.x or a.x
    2) the descriptor is not invoked by direct dictionary access: p1.__dict__['x']
    3) the __get__() and __set__() methods normally eventually delegate to the object class to extract the
       relevant attribute.  However, you don't have call these object methods if you so desire.
    4) the attribute hook __getattribute__ doesn't use __dict__ and hence will trigger the descriptor protocol
       but the other attribute hooks do use __dict__ and hence bypass the descriptor protocol
'''

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

o = object()
pass







