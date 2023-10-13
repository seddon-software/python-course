'''
Slicingxxxx
=======

As with ordinary Python arrays (list and tuple) we can use slicing. The notation in Numpy is slightly different 
from normal - all the slicing parameters are enclosed in a single set of [ ] brackets.

We can also slice multi-dimensional arrays.  In the following example we slice elements 0 and 1 of each dimension.
Thus we will end up with a 2x2x2 array:
'''

import numpy as np

# one dimensional arrays
a = np.arange(20); print(a)
print(a[7:14])
print(a[2:14:3])
print(a[::])
print()

# multi-dimensional arrays
a = np.arange(24).reshape(4,3,2); print(a)
print(a[0:2,0:2,0:2])

