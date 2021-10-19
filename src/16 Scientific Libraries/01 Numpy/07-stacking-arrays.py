############################################################
#
#    stacking arrays
#
############################################################

import numpy as np

a = np.ones( (3,5) ); print(a)
b = np.zeros( (3,5) ); print(b)

print("stacking")
h = np.hstack( (a,b) ); print(h)
v = np.vstack( (a,b) ); print(v)


