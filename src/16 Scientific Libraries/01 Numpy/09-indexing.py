############################################################
#
#    indexing
#
############################################################

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
filter = a % 3 == 0; print(filter)
a[filter] = 99; print(a)

filter = a[:,:] % 3 == 0; print(filter)
a[filter] = 88; print(a)



1

