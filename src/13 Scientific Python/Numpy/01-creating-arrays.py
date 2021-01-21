############################################################
#
#    creating arrays
#
############################################################

import numpy as np

np.set_printoptions(precision=3)

# create array filled with 1's
a = np.ones( (3,5) ); print(a)
b = np.ones( (3,5) ) * 13; print(b)

# create array filled with 0's
a = np.zeros( (3,5) ); print(a)

# create empty array
a = np.empty( (3,5), dtype=int); print(a) 

# create array from a list
a = np.array( [2,3,5,7,11,13,17] ); print(a)
a = np.array( [ [3,4],[5,6] ]); print(a)

# create array with random values
a = np.array( np.random.random((2,3)) ); print(a)

# create using arange
a = np.arange(4.0);      print(a)
a = np.arange(4.0,17.0);   print(a)
a = np.arange(4.0,6.0,0.1); print(a)

# create equally spaced arrays
a = np.linspace(-50.0,50.0,5); print(a)
a = np.linspace(-50.0,50.0,7); print(a)


1
