'''
isinstance
==========
We can check if an object is an instance of a class or group of classes using this built in method.  The method
will also return true if the object is derived from the class specified.
'''

class A(object):
    pass

class B(A):
    pass

class C(A):
    pass


a = A()
b = B()
c = C()

print("classes B and C are derived from A")

if isinstance(a, (A,B,C)):
    print("a is an instance of A, B, or C")

if isinstance(b, (A,B,C)):
    print("b is an instance of A, B, or C")
    
    
if isinstance(c, A):
    print("c is an instance of A")
if not isinstance(c, B):
    print("c is NOT an instance of B")
if isinstance(c, C):
    print("c is an instance of C")
