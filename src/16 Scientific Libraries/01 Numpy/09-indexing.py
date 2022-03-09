'''
Indexing
========

Although we can use slicing with Numpy arrays, sometimes it is useful to work with parts of an array that (unlike 
with slicing) are not all adjacent.  Indexing allows us to do this.  As we will see later, this has important
application in Image Processing.

An index is just another Numpy array and can have any number of dimensions:
            index1 = np.array( [2,3,5,9] ); print(index1)
            index2 = np.array( [[5,9],[2,3]]); print(index2)

The index can then be used with a further Numpy array to select parts of the array.  In the example below we create 
a 6x4 array and index it with the above indexes to pull out parts of "a".

Finally, we create a boolean index: 
            filter = (a % 3 == 0)

This computes boolean values for all 24 points of "a", giving an index of:
            [[ True False False  True]
            [False False  True False]
            [False  True False False]
            [ True False False  True]
            [False False  True False]
            [False  True False False]]

When applied to a the index acts as a filter:
            a[filter] = 99

this sets all values of "a" where the filter is True to 99.
            [[99  1  2 99]
            [ 4  5 99  7]
            [ 8 99 10 11]
            [99 13 14 99]
            [16 17 99 19]
            [20 99 22 23]]
'''

import numpy as np

# set up an array to be used in indexing
a = np.arange(10)**2; print(a)

# setup index arrays
index1 = np.array( [2,3,5,9] ); print(index1)
index2 = np.array( [[5,9],[2,3]]); print(index2)

# apply indexes to a
print(a[index1])
print(a[index2])

# set up a boolean filter for a
# filter is applied for each element of a; a is shortform of a[:,:]
a = np.arange(24).reshape(6,4); print(a)
filter = (a % 3 == 0); print(filter)
a[filter] = 99; print(a)

# alternative notation
filter = a[:,:] % 3 != 0; print(filter)
a[filter] = 88; print(a)





