############################################################
#
#    splitting arrays
#
############################################################

import numpy as np

a = np.array( np.random.random((3,5)) * 100 ); 
a = np.round(a, 2); print(a)

print("split horizontally")
a0,a1,a2,a3,a4 = np.hsplit(a,5)
print(a2)

print("split vertically")
a0,a1,a2 = np.vsplit(a,3)
print(a)
print(a1)

print("split unequal horizontally")
a0,a1,a2 = np.hsplit(a,(2,3))  # split at col 2 and 3
print(a)
print("a0 ="); print(a0)
print("a1 ="); print(a1)
print("a2 ="); print(a2)


1