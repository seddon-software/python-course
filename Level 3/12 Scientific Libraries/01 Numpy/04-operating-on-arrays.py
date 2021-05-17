############################################################
#
#    operating on arrays
#
############################################################

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


1
