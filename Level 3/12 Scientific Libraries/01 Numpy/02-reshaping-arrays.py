############################################################
#
#    reshaping arrays
#
############################################################

import numpy as np

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

1
