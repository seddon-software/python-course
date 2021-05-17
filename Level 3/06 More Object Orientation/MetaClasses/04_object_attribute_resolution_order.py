# This example shows how attributes are resolved for objects

class A(object):
    x1 = 1
    
class B(A):
    x2 = 2
    
class C(B):
    x3 = 3
    
a = A()
b = B()
c = C()
a.y1 = 11
b.y2 = 22
c.y3 = 33

# lookup chain for attributes starts with the object, 
# then each class in inheritance tree using method resolution order (MRO)

print(A.mro())
print(a.y1)     # attribute of a object 
print(a.x1)     # attribute of A class

print(B.mro())
print(b.y2)     # attribute of b object 
print(b.x2)     # attribute of B class
print(b.x1)     # attribute of A class

print(C.mro())
print(c.y3)     # attribute of c object 
print(c.x3)     # attribute of C class
print(c.x2)     # attribute of B class
print(c.x1)     # attribute of A class
