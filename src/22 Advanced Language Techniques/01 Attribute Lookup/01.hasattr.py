'''
Has Attribute
=============

The hasattr is a useful builtin.  As the name implies, the function checks and object to see if it has a given
method.  
'''

class MyClass:
    def f1(self): print("this is f1()")
    def f3(self): print("this is f3()")

obj = MyClass()

# check against the class
print(f"has MyClass got a method f1: {hasattr(MyClass, 'f1')}")
print(f"has MyClass got a method f2: {hasattr(MyClass, 'f2')}")
print(f"has MyClass got a method f3: {hasattr(MyClass, 'f3')}")

# check against an object instance, before calling method
if hasattr(obj, "f1"): obj.f1()
if hasattr(obj, "f2"): obj.f2()     # no f2 method so nothing called
if hasattr(obj, "f3"): obj.f3()     

