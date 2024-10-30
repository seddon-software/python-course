import os; os.system("clear")
'''
Using Lambdas
=============

Lambdas are another way of defining a function object.  An important difference from ordinary functions is
that they can't have a body.  Another difference is that they are an expression as opposed to a statement.

Because they are an expression, they can be defined as parameters to a function.  This is very useful if
you only need the lambda once; you can define it and use it in one place.  This saves creating a "def" 
somewhere in the code an invoking later.  This is a typical use case for lambdas: define and use in one place.

At the end of this example, we've decided to raise a number to its seventh power.  It is unlikely that we will
need this function again, so rather than going to the trouble of creating a "def", we just use a one-off lambda.  
'''

def square(x):
    return x**2

def cube(x):
    return x**3

def quad(x):
    return x**4

def powers(fn, n):
    return fn(n)

print( powers(square, 5) )
print( powers(square, 7) )
print( powers(square, 9) )
print( powers(cube, 6) )
print( powers(cube, 8) )
print( powers(cube, 10) )
print( powers(quad, 13) )
print( powers(quad, 15) )
print( powers(quad, 17) )

# raising to the seventh power will only be used once
# so just provide a lambda
print( powers(lambda x:x**7, 2))
