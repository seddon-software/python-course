############################################################
#
#    rebinding objects to another class
#
############################################################

class A(object):
    def f(self):
        print("calling f()")

class B(object):
    def g(self):
        print("calling g()")


# create instance
a = A()             # a is bound to class A
a.f()
a.__class__ = B     # rebind to class B

try:
    a.g()   # this will succeed
    a.f()   # this call will fail
except Exception as e:
    print(e)

1
