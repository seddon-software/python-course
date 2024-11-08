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
    x = "class dict of A"
    y = "class dict of A"
    z = "class dict of A"
    def __init__(self):
        self.x = "dict of A object"
        self.y = "dict of A object"
        self.z = "dict of A object"

class B(A):
    x = "class dict of B"
    y = "class dict of B"
    def __init__(self):
        A.__init__(self)
        self.x = "dict of B object"
        self.y = "dict of B object"

class C(B):
    x = "class dict of C"
    def __init__(self):
        B.__init__(self)
        self.x = "dict of C object"

print("class attribute lookup traverses the inheritance hierarchy")
print(f"class attribute C.x found in: {C.x}")    
print(f"class attribute C.y found in: {C.y}")    
print(f"class attribute C.z found in: {C.z}")
print()

print("object attribute lookup also traverses inheritance hierarchy")
o = C()
print(f"o.x found in {o.x}")
print(f"o.y found in {o.y}")
print(f"o.z found in {o.z}")
print()

    