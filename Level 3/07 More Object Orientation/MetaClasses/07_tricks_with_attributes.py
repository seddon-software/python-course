############################################################
#
#    mro
#
############################################################

class A(object):
    x = 100
    
class B(A):
    pass

class C(B):
    def f(self):
        # this strange construct actually creates a new attribute
        # self.x on RHS picks up x from base class
        # self.x on LHS adds a reference to instance of C
        # now we have two distinct references
        self.x = self.x         # !!! not what it seems !!!
        self.x = 200

c = C() # reference (x) only exists in base class
print(A.x)
print(c.x)
print(id(A.x))
print(id(c.x))

c.f()   # create a second reference
# prove the references are distinct
print(A.x)
print(c.x)
print(id(A.x))
print(id(c.x))

1