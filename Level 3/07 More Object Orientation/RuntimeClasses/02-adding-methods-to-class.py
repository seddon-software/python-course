import types

# create a class that can dynamically add and remove methods
class MyClass(object):
    @classmethod
    def removeMethod(cls, name):
        return delattr(cls, name)

    @classmethod
    def addMethod(cls, func):
        return setattr(cls, func.__name__, types.MethodType(func, cls))

    @classmethod
    def addLambda(cls, name, func):
        return setattr(cls, name, types.MethodType(func, cls))

m = MyClass()

# add methods to the class
def square(self, x): return x**2
MyClass.addMethod(square)
MyClass.addLambda("cube", lambda self, x : x**3)

# check the dictionary
print((MyClass.__dict__))

# invoke methods
print((m.square(6)))
print((m.cube(5)))

# remove methods
MyClass.removeMethod("square")
MyClass.removeMethod("cube")

# these calls will now fail
try: m.square(7); 
except: print("square failed")
try: m.cube(8)
except: print("cube failed")

