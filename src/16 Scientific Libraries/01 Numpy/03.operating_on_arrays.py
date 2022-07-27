'''
Operating on Arrays of the Same Size
====================================

In Numpy you can perform matrix arithmetic on 2 dimensional arrays (see later examples).  However, if the arrays 
are not 2 dimensional then this wouldn't work in the general case. The @ sign is reserved for matrix multiplication. 
All other mathematical operators and functions are performed element by element on Numpy arrays.

It is easy to see how this scheme works on arrays of the same size. Consider the following operations with 1 
dimensional arrays.  Peforming calculations, element by element, on "a" and "b" of shape=(7,) means performing 
7 separate calculations:
    3 * 5 + 2 = 17
    3 * 5 + 2 = 17
    3 * 5 + 2 = 17
    3 * 5 + 2 = 17
    4 * 6 + 2 = 26
    3 * 5 + 2 = 17
    3 * 5 + 2 = 17
and storing the answers in "c".

We'll leave what to do about arrays of different sizes until later.
'''

import numpy as np
np.set_printoptions(precision=3)


a = np.array( [3,3,3,3,4,3,3] )
b = np.array( [5,5,5,5,6,5,5] )

# operations are performed on each element
c = a * b + 2
print(c)


# dot and cross product
a = np.array( [[ 2,4], [3,5]] )
b = np.array( [[ 0,1], [1,0]] )
c = np.dot(a,b); print(c)
c = np.cross(a,b); print(c)
print()



