'''
Broadcasting
============

When operating on arrays of different sizes or dimensions, Numpy can't immediately do element by element calculations.  Instead
Numpy has to modify the input arrays such that they become the same size.  This procedure is called broadcasting.

Lets see how Numpy uses broadcasting with a one dimensional X array:
                [1 2 3 4 5 6]

and a two dimensional Y array (of different size from X):
                [[1]
                 [2]
                 [3]
                 [4]]

Lets say we want to calculate a resulting array Z:
                Z = (X + Y)**2 

Numpy realizes that it needs to change X into a 2D array with the same number of rows as Y.  It therefore duplicates the first and only row of X
to create a 4 x 6 array.  The duplication is termed broadcasing.  The new array looks like:
            [[1 2 3 4 5 6]
             [1 2 3 4 5 6]
             [1 2 3 4 5 6]
             [1 2 3 4 5 6]]

Likewise, with Y; Numpy duplicates the first column:
            [[1 1 1 1 1 1]
             [2 2 2 2 2 2]
             [3 3 3 3 3 3]
             [4 4 4 4 4 4]]

Now the two arrays are both the same size (4 x 6) and Numpy can now proceed with element by element calculation, resulting in:
        Z = [[  4   9  16  25  36  49]
             [  9  16  25  36  49  64]
             [ 16  25  36  49  64  81]
             [ 25  36  49  64  81 100]]

If you think about it, the Z array contains the heights of the function (x + y)**2 for each point in the x, y plane.  Therefore if we plot Z
we will get a surface plot of this function.

We will use matplotlib to perform the surface plot. The plot function we will use is as follows:

    ax.plot_surface(X, Y, Z, cmap)

The X and Y parameters must both be 2 dimensional arrays that encompass all points in the xy plane that we wish to 
use in our surface plot. In our case that's the 24 points.  As we've seen the Z values  be computed from the X an Y arrays 
for each of our 24 points. The colormap is used to give artificial colors to the surface to make it easier to 
visualise.
'''

import numpy as np

X = np.arange(1,7)
Y = np.arange(1,5).reshape((4,1))
print(f"X=\n{X}")
print(f"Y=\n{Y}")
print(f"X has shape {X.shape}")
print(f"Y has shape {Y.shape}")

print("\nbroadcast X and Y, because arrays are different sizes and dimensions and then compute Z")
Z = (X + Y)**2 
print(f"Z=\n{Z}")
print(f"Z has shape {Z.shape}")

# now visualize the surface
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Y, Z, cmap=cm.flag)
plt.show()
