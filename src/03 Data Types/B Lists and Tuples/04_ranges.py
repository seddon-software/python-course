'''
range
=====
range is a generator that produces a range object.  These objects are easily cast to form a tuple of sequentual
integers.  The range generator can have up to 3 parameters:
            range(lower-bound, upper-bound, step)

range cannot produce sequences of floats, but the numpy library has an array range function (arange) that does 
produce a sequences of floats.

Note that the upper bound is excluded from the generated list for both range and arange.
'''

# create a range object
r = range(50)
print(type(r))
print(len(r))       # r is automatically cast to a list to calculate length
print(r)
print(list(r))      # cast to list

# specify lower and upper bound and step
x = list(range(10, 15, 2))
y = list(range(20, 1, -3))        # step can be negative
print(x)
print(y)

# working with floats requires the numpy module
import numpy as np
print(np.arange(1.5, 3.7, 0.1))  # step by 0.1

