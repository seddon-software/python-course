############################################################
#
#    basic functions
#
############################################################

import numpy as np
np.set_printoptions(precision=3)


a = np.array( np.random.random(12) * 100, dtype="int" ).reshape(3,4)
print(a)

# perform operations along specified axis
print(np.average(a, axis=0))
print(np.average(a, axis=1))

# sort data
print(np.msort(a))
print(np.sort(a, axis=0))
print(np.sort(a, axis=1))

# insert elements:  insert(array, positions, items)
print(a)
b = np.insert(a, (1,5,9), (-1,-2,-3) ); print(b)
b = np.insert(a, (1,5,9), (-1,-2,-3) ).reshape(3,5); print(b)
b = np.append(a, (-1,-2,-3,-4) ).reshape(4,4); print(b)

b = np.round_(a ** 1.1, 2); print(b)

1
