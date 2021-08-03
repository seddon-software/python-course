############################################################
#
#    rebinding objects to another class
#
############################################################

class A(object):
    def f(self):
        print("calling A.f()")

class B(object):
    def g(self):
        print("calling B.g()")


# create instance
a = A()             # a is bound to class A
a.f()
a.__class__ = B     # rebind to class B

try:
    a.g()   # this will succeed (g is method of class B)
    a.f()   # this call will fail
except Exception as e:
    print(e)

1
