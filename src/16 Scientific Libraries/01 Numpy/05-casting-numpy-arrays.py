'''
Casting Numpy Arrays
====================

Sometimes we need to change the type of data in a Numpy array.  For example, with images, pixel values can be 
stored as decimal (from 0.0 to 1.0) or as integers (0 to 255).  If we are creating a black and white image, we 
might set the array up with integers 0 or 1 and then convert the array to floats.  Such operations are called 
casts.

Below are some examples.  Note the use of the "fromfunction" method.  This method calls a function (lambda) to 
calculate the value of each element in the array.  Since we are creating a (4,4) array, there will be 16 
calculations to perform.  The "i" and "j" inputs to the lambda witll vary from 0 to 3, and calculate:
            (i+2) * (j+2)**1.4
'''

import numpy as np
np.set_printoptions(precision=3)

# start with a float64 array
array1 = np.fromfunction(lambda i,j: (i+2)*(j+2)**1.4, (4,4))
print(array1.dtype)
print(array1)

# casting creates a new array of int
array2 = array1.astype(int)
print(array2.dtype)
print(array2)

# casting creates a new array of bool
array3 = array1.astype(bool)
print(array3.dtype) 
print(array3)
