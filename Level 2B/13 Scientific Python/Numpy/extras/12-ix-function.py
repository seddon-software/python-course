############################################################
#
#    ix function
#
############################################################

import numpy as np

# The ix_ function takes N 1-D sequences and returns N outputs
# with N dimensions each, such that the shape is 1 in all but 
# one dimension and the dimension with the non-unit shape value 
# cycles through all N dimensions.

# set up arrays to be used for 3D grid
a = np.array([2,5,7])
b = np.array([4,8,1])
c = np.array([3,5,2])

ax,bx,cx = np.ix_(a,b,c)
print(ax)
print(bx)
print(cx)
result = ax * (bx + cx) # uses broadcasting to become a 3 x 3 array
print(result)

# then these are equivalent
print(result[1,2,1])
print(a[1] * (b[2] + c[1]))

1

