'''
In Python functions are first class objects.  This means functions behave like any other object and can have
methods and attributes.  Recall that all objects are anonymous in Python, so you need an object reference
to point at a function object.

In this example we define a function object with an attribute 'x'.  All is well accessing this attribute until
the reference to the function object is changed and the original reference deleted:
            g = f
            del f       # reference f is now invalid

Access to the attribute was tided to "f", but after "f" is deleted there seems to be no way to access the "x"
attribute.  Note however, the attribute is still accessible through __dict__.

As we will see later, the "x" attribute can only be retreived by using the "inspect" ans "dis" modules.
'''


import inspect
import dis

# this function prints its 'x' attibute, but it fails if the original 
# function name is deleted (see below)
def f():
    print(f.x)

f.x = 'foo'
f()         # print the "x" attribute

# change the object reference
g = f
del f       # reference f is now invalid

# now call the function through the new reference
# we get an exception because the attribute was bound to the original name 'f'
try:
    g()
except NameError as e:
    print(f"We don't know the current name of the function: {e}")

# note: functions are regular objects, so we can still see attributes through __dict__
print(g.__dict__['x'])
