############################################################
#
#    broadcasting
#
############################################################

import numpy as np

X = np.arange(1,7)
Y = np.arange(1,5)
print("X and Y are 1D arrays")
print(X)
print(Y)

Y = np.vstack(Y)
print("\nY is now a 2D array")
print(Y)
print("\nX is still a 1D array")
print(X)

print("\nbroadcast X and Y, because arrays are different sizes")
M = X * Y 
print(M)


1

