'''
For a given class you can easily find out a list of immediate base (super) classes using the "__bases__" attribute.  In this example the
class "MyClass" uses multiple inheritance and hence has several base classes.

                    X
                    ^
                    |
                    |
            A   B   C
            |   |   |
            |   |   |
            \   |   /
             \  |  /
              \ | /
               \|/
             MyClass

'''

class X : pass
class A : pass
class B : pass
class C(X) : pass
class MyClass(A,B,C): pass

m = MyClass()

# what are the immediate super classes
print(f"immediate super classes of {m.__class__.__name__}: ")
for clazz in MyClass.__bases__:
    print(f"{clazz.__name__}", end=", ")
print()

