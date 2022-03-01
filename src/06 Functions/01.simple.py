'''
Function Objects
================

Functions in Python are a little different to functions in other languages.  Python functions are objects, rather
than just code.  Think of a Python function in terms of the bytecode that represents the function.

We will look at what this means in practice with later examples.  For now we simply define a function object
and call the function 3 times.  Note we can pass parameters to functions using () brackets.  If you are familiar
with how parameters are passed in other languages, then in Python parameters are passed by copy (value).

The keyword def is used to introduce a function.
'''

def square(n):      # this creates a pointer: square and bytecode for the function object
    print(n**2)


square(5)
square(6)
square(7)


