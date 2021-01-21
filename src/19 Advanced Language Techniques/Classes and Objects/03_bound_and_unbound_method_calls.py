############################################################
#
#    bound and unbound method calls
#
############################################################

class A(object):
    def f(self):
        pass
    def g():
        pass

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

try:
    A.g()   # fails without instance parameter
except Exception as e:
    print(e)

1
