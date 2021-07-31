############################################################
#
#    isinstance
#
############################################################

class A(object):
    pass

class B(A):
    pass

class C(A):
    pass


a = A()
b = B()
c = C()

if isinstance(a, (A,B,C)):
    print("instance of A, B, or C")

if isinstance(b, (A,B,C)):
    print("instance of A, B, or C")
    
if isinstance(c, C):
    print("instance of C")
    
1
