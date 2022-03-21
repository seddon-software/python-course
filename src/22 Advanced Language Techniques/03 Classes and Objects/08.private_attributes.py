'''
Private Attributes
==================
Many languages allow you to encapsulate object attributes by making them private.  This is not the Python way.
However, if you insists, there is a way ...

The trick is to create a dictionary in init that is pointed at by a local variable and then define getters and
setters using this dict before the dictionary goes out of scope.  Pointers to the getters and setters need to 
be added to the normal object dictionary to make them available outside the class.

Now all object access will have to be made via the getters and setters; x and y are not visible in the main
program.
'''

class MyClass:
    def __init__(self):
        # data is fully encapsulated - can't be seen outside the class
        data = {}
        # these methods can access data by closure
        def dogetX(): return data['x']
        def dogetY(): return data['y']
        def dosetX(x): data['x'] = x
        def dosetY(y): data['y'] = y
        # these attributes belong to each object, not the class
        self.dogetX = dogetX
        self.dogetY = dogetY
        self.dosetX = dosetX
        self.dosetY = dosetY
    def __str__(self):
        return f"x={self.dogetX()}, y={self.dogetY()}"
m1 = MyClass()
m2 = MyClass()
m1.dosetX(100)
m1.dosetY(101)
m2.dosetX(200)
m2.dosetY(201)
print(m1.dogetX())
print(m1.dogetY())
print(m2.dogetX())
print(m2.dogetY())
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
