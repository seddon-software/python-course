'''
Has Attribute
=============

The hasattr is a useful builtin.  As the name implies, the function checks and object to see if it has a given
attribute (method is considered as an attribute).  
'''

class MyClass:
    def f1(self): print("this is f1()")
    def f3(self): print("this is f3()")

obj = MyClass()

# check against the class
print(f"has MyClass got a method f1: {hasattr(MyClass, 'f1')}")
print(f"has MyClass got a method f2: {hasattr(MyClass, 'f2')}")
print(f"has MyClass got a method f3: {hasattr(MyClass, 'f3')}")


