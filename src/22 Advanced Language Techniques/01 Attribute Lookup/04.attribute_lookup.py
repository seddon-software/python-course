'''
Attribute Lookup
================
The rules for attribute lookup are different for l-values (things appearing on the left hand side of =) and r-values
(things appearing on the right hand side of =).

Consider first the lookup strategy Python uses for class attributes.  The inheritance hierarchy defines 3 class
attributes x, y and z, but z is defined in all 3 classes, y in 2 classes and z only in the base class.  When we
lookup C.x it is found in class C, but the lookup of C.y shows that since y is not present in C, Python goes on
to search the parent class and finds the attribute in B.  With C.z Python searches all the way up the inheritance 
hierarchy until if find x in A.  

The rule for l-value class lookup:
    
    If a class attribute is missing from the class's dictionary then successive superclasses are searched until 
    the attribute is found.

A similar picture exists with object lookup.  

The rule for l-value object lookup:
    If an object attribute is missing from the object's dictionary then successive superclasses are searched until 
    the attribute is found.
'''

class A:
    x = "class attribute of A"
    y = "class attribute of A"
    z = "class attribute of A"
    def __init__(self):
        self.x = "object attribute of class A"
        self.y = "object attribute of class A"
        self.z = "object attribute of class A"

class B(A):
    x = "class attribute of B"
    y = "class attribute of B"
    def __init__(self):
        A.__init__(self)
        self.x = "object attribute of class B"
        self.y = "object attribute of class B"

class C(B):
    x = "class attribute of C"
    def __init__(self):
        B.__init__(self)
        self.x = "object attribute of class C"

print("dotted class lookup traverses inheritance hierarchy")
print(f"C.x found: {C.x}")    
print(f"C.y found: {C.y}")    
print(f"C.z found: {C.z}")
print()

print("dotted object lookup traverses inheritance hierarchy")
o = C()
print(o.x)
print(o.y)
print(o.z)
print()

print("direct dictionary lookup works the same way")
print(o.__dict__['x'])
print(o.__dict__['y'])
print(o.__dict__['z'])
    