############################################################
#
#    slicing and iterating
#
############################################################

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

