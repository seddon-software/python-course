'''
Private Attributes
==================
Many languages allow you to encapsulate object attributes by making them private.  The attempt in the
previous example is easily circumvented.  This is not the Pythonic way.

However, if you insist, there is a way ...

The trick is to create a dictionary in __init__() that is pointed at by a local variable and then define getters
and setters using this dict before the dictionary goes out of scope.  Pointers to the getters and setters need to 
be added to the normal object dictionary to make them available outside the class.

Now all object access will have to be made via the getters and setters; x and y are not visible in the main
program.
'''

class Point:
    def __init__(self, x0, y0):
        # data is fully encapsulated - can't be seen outside the class
        data = {'x':x0, 'y':y0}
        # these methods can access data by closure
        def getX(): return data['x']
        def getY(): return data['y']
        def setX(x): data['x'] = x
        def setY(y): data['y'] = y
        # these attributes belong to each object, not the class
        self.getX = getX
        self.getY = getY
        self.setX = setX
        self.setY = setY
    def moveBy(self, dx, dy):
        x = self.getX()
        y = self.getY()
        x += dx
        y += dy
        self.setX(x)
        self.setY(y)
    def __str__(self):
        return f"x={self.getX()}, y={self.getY()}"
m1 = Point(5, 10)
m2 = Point(2, 20)
print(m1)       # call m1.__str__()
print(m2)       # call m2.__str__()

m1.setX(100)
m1.setY(101)
m2.setX(200)
m2.setY(201)
print(m1)
print(m2)

# call a method
m1.moveBy(1, 3)
m2.moveBy(11, 22)
print(m1)
print(m2)

# x and y are not visible
try:
    print(m1.x)
except Exception as e:
    print(e)
try:
    print(m1.y)
except Exception as e:
    print(e)

