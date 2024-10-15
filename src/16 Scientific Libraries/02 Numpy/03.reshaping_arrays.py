############################################################
#
#    reshaping arrays
#
############################################################
'''
All Numpy arrays are stored as 1 dimensional arrays, irrespective of their real dimensionality. The data in the 
array is pointed at by a structure called the "view" which contains, amongst other things, this dimensionality 
information.

In the following example we create two Numpy arrays sharing the same set of data, but having different views. The 
first array is created with "arange" and the second is a shallow copy of the first, but with its dimensionality 
changed using the "resize" function.

"arange" is Numpy's version of the range generator. And no, its not a mispelling of "arrange"; it stands for 
"array range". Where it differs from the built in "range" generator is that it can be used with floating point
numbers.

"reshape" takes an existing Numpy array and creates a new view on the same data. The idea is that the new view 
contains different dimensionality data. Since the data is unchanged, the new dimensions must contain the same 
number of data points as the original array. Thus in the example below, we start with a 1 dimensional array 
with 24 elements and reshape it to a 3 dimensional array with 2 * 3 * 4 = 24 elements. 

At he end of the example, we take a look at properties stored in the view.
'''

import numpy as np
import os
os.system("clear")

# create array
a = np.arange(24); print(a)
# reshape it
b = a.reshape(2,3,4); print(b)
a[13] = 99
print(a)
print(b)
# display properties held in the view
print(type(b))
print("Shape:", b.shape)
print("Dimensions:", b.ndim)
print("Size:", b.size)
print("Item type:", b.dtype.name)
print("Item size:", b.itemsize)


