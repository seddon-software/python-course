'''
Rebinding Objects to Another Class
==================================
The __class__ attribute of a object points at the class structure.  Surprisingly, this attribute is mutable.
This in turn means an object can change its class at run-time!  Although not recommended (most programmers are
unaware you can do this) it is perfectly valid as this example illustrates.

Once an object changes its class it will only be able to invoke methods of its new class.
'''

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


