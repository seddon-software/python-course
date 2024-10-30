import os; os.system("clear")
'''
Partial Functions
=================

Partial functions allow us to fix a certain arguments of a function and generate a new function.
The new function can then be called with values supplied for the missing parameters.

We use partial functions in situations where you only know the values of some parameters and you need
to pass the partial function as a parameter to another function for a callback.  Then by the time the callback 
is made, the remaining parameters are known and can be supplied to the partial function. 
'''

import functools as ft

# return a new function which behaves like the original function with some parameters filled in
# range takes 3 parameters
myrange = ft.partial(range, 0, 10) # 2 parameters filled in
print((list(myrange())))
print((list(myrange(2)))) # supply a 3rd parameter

# now try with a function of 5 parameters
def f(v, w, x, y, z): return v + w + x + y + z

f1 = ft.partial(f, 10, 20)  # f1 takes 3 more parameters
print((f1(30, 40, 50)))

f2 = ft.partial(f1, 30)
print((f2(40, 50)))
