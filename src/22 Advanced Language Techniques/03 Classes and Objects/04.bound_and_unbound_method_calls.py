'''
Bound and Unbound Method Calls
==============================
You may come across the terms bound and unbound method calls.  A bound method call is simply one that is invoked
via an object.  A unbound method call is one invoked through a class (no self parameter).  The term unbound
method tends not to be used in Python 3 because it is regarded as confusing.  
'''

class A(object):
    def f(self):
        print("instance method")
    def g():
        print("class method - no self")

# create instance
a = A()

# unbound methods (not bound to an instance - just a class)
print(A.f)
print(A.g)
# bound methods (bound to an instance)
print(a.f)
print(a.g)

A.f(a)  # how to call an unbound method (note instance parameter)
a.f()   # how to call a bound method
A.g()   # class method (no instance parameter)


