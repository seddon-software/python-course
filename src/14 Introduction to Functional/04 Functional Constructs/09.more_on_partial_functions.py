'''
Partial Functions
=================

One application of nested functions and closures is that it allows us to create partial functions.  This is
encapsulated in the "functools" Python library:
            from functools import partial

Here we define a function "f" with a nested function "g".  The nested function uses the closure of x in the 
calculation of its return value.  Note how "f" returns "g".  "g" takes just 2 parameters, so we have created
a function derived from "f" where the value of x doesn't need to be passed, i.e. a partial function.
'''

def f(x):
    def g(y, z):    # this function knows about the value of x using a closure
        return x + y + z
    return g

f15 = f(15)   # f15 points to a function returning 15 + y + z
f20 = f(20)   # f20 points to a function returning 20 + y + z
f25 = f(25)   # f25 points to a function returning 25 + y + z
f50 = f(50)   # f50 points to a function returning 50 + y + z

print( f15(1,2) )  # prints 15 + 1 + 2 = 18
print( f15(7,9) )  # prints 15 + 7 + 9 = 31
print( f20(1,2) )  # prints 20 + 1 + 2 = 23
print( f20(7,9) )  # prints 20 + 7 + 9 = 36
print( f25(1,2) )  # prints 25 + 1 + 2 = 28
print( f25(7,9) )  # prints 25 + 7 + 9 = 41
print( f50(1,2) )  # prints 50 + 1 + 2 = 53
print( f50(7,9) )  # prints 50 + 7 + 9 = 66

