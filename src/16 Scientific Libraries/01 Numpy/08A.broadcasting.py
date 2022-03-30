'''
Broadcasting
============

We can use Numpy in conjunction with MatPlotLib to produce surface plots of 3 dimensional arrays.
Numpy uses broadcasting when arrays are different sizes.  Let's work through an example of creating a surface plot 
that utilises Numpy's broadcasting.

We are going to create a surface plot of a function dependent on these variables X and Y.

The X variable ranges between 1 and 6 and the Y variable between 1 and 4. This means we will have 6 * 4 = 24 points 
in the xy plane.

We will use matplotlib to perform the surface plot. The plot function we will use is as follows:

    ax.plot_surface(X, Y, Z, cmap)

The X and Y parameters must both be 2 dimensional arrays that encompass all points in the xy plane that we wish to 
use in our surface plot. In our case that's the 24 points.  The Z values will be computed from the X an Y arrays 
for each of our 24 points. The colormap is used to give artificial colors to the surface to make it easier to 
visualise.

The X array has to contain the values of x for each of the 24 points.  Numpy expands the one dimensional array X
to a 4x6 two dimensional array by duplication the first row (i.e. broadcasting it):
            [[1 2 3 4 5 6]
            [1 2 3 4 5 6]
            [1 2 3 4 5 6]
            [1 2 3 4 5 6]]

Similarly with Y; Numpy duplicates the first column:
            [[1 1 1 1 1 1]
            [2 2 2 2 2 2]
            [3 3 3 3 3 3]
            [4 4 4 4 4 4]]

Now Numpy can easily compute Z:
            [[  4   9  16  25  36  49]
            [  9  16  25  36  49  64]
            [ 16  25  36  49  64  81]
            [ 25  36  49  64  81 100]]
'''
'''
Y = [1 1 1 1 1 1
     2 2 2 2 2 2
     3 3 3 3 3 3
     4 4 4 4 4 4]
x = [1 2 3 4 5 6]
     1 2 3 4 5 6
     1 2 3 4 5 6
     1 2 3 4 5 6
'''
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
M = (X + Y)**2 
print(M)



