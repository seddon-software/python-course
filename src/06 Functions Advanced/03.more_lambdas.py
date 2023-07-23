'''
More Lambdas
============
Here we show how to pass a lambda to another function object
            power(lambda x:x**n, 2)

Lambdas can be used in this way to define new functions "on the fly".  For example, if n is 8 then
            power(lambda x:x**n, 2)
passes lambda x:x**8 as the first parameter to power.  Thus we define raising to the 8th power "on the fly".
'''


def square(x):
    return x**2

def cube(x):
    return x**3

def quad(x):
    return x**4
    
def power(fn, x):
    return fn(x)

n = int(input("enter a power: "))
print(power(lambda x:x**n, 2))
