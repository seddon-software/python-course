'''
Function Parameters
===================

There are two ways parameters can be passed to a function object:
    1. positional or 
    2. named
or a combination of both.  With positional parameters, order is of utmost importance.  With
            def f(a, b, c):

considering the call:
            print(f(2, 4, 8))

Then then first parameter (2) is copied to a (or rather a points to the object 2), the second parameter (4) is
copied to b and lastly 8 is copied to c.  This is the time honoured way to pass parameters to functions and is 
the mechanism used in most high level languages.

On the other hand, named parameters, make it explicit which parameter is which and named parameters have the 
advantage that they do not rely on ordering.  Thus
            print(f(c = 3, a = 1, b = 2), end=' ')
            print(f(b = 2, c = 3, a = 1), end=' ')
are entirely equivalent.
'''

def f(a, b, c):
    return a + b + c

print(f(1, 2, 3))

# positional parameters
print(f(1, 1, 1), end=' ')
print(f(1, 2, 3), end=' ')
print(f(2, 4, 8))

# named parameters
print(f(a = 1, b = 1, c = 1), end=' ')
print(f(c = 3, a = 1, b = 2), end=' ')
print(f(b = 2, c = 3, a = 1), end=' ')
print(f(c = 8, b = 4, a = 2))
