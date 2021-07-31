############################################################
#
#    function names
#
############################################################


import inspect
import dis
import re
import sys
import io

# this function prints its 'x' attibute, but it fails if the original 
# function name is changed (see below)
def f():
    print(f.x)

f.x = 'foo'
f()

# change the object reference
g = f
del f       # reference f is now invalid

# now call the function through the new reference
# we get an exception because the attribute was bound to the original name 'f'
try:
    g()
except NameError as e:
    print("don't know the current name of the function")
    print(e)

# functions are regular objects, so we can still see attributes through __dict__
print(g.__dict__['x'])
