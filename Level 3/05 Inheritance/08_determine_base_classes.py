class X : pass

class A : pass
class B : pass
class C(X) : pass

class MyClass(A,B,C): pass

m = MyClass()

# what is the class of an object
print(f"class name of m: {m.__class__.__name__}")

# what are the immediate super classes
print("immediate super classes:")
for clazz in MyClass.__bases__:
    print(f"{clazz.__name__}", end=", ")
print()

