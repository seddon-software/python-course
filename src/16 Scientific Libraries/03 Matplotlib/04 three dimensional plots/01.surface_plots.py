'''
Surface Plots
=============

MatPlotLib makes it relatively easy to create surface plots of a 3D function.  In this example we take the
longhand route to creating a surface plot so we can see how things work.

To begin with we have to create 2 sets of entries (X and Y) for defining each point on the z=0 plane.  We need 
a 2D array for the values of x at each point on the plane and we also need a 2D array for the values of y at each 
point on the plane.

If you study the X array you will notice each column has the same data.  This is because each column corresponds
to a different value of y.  Similarly each row of the Y array is identical, corresponding to different values of x.
Once these two arrays are defined we have to compute the z values (the height of the plot at any (x, y) point.
We can simply use Numpy's vector calculations for this as in:
                R = np.sqrt(X**5 + 8*X*Y**0.5)
                Z = np.sin(R)
The trigonometric functions are just there to make the surface plot more interesting.  Given that the X aray is 
11x11 and the same for the Y array, the Z array will also be 11x11.

In practice, we can generate the X and Y arrays in a much simpler way (see subsequent examples).
'''
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# X and Y must be 2D arrays.
# X entries show the value of x at each point on the XY plane 
# Y entries show the value of y at each point on the XY plane 

X = np.array([
    [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
    [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
    [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
    [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
    [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
    [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
    [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
    [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
    [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
    [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
    [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]])

Y = np.array([
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
    [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2],
    [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3],
    [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4],
    [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],
    [0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6],
    [0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7],
    [0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8],
    [0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]])

R = np.sqrt(X**5 + 8*X*Y**0.5)
Z = np.sin(R)
print(f"shape of X = {X.shape}")
print(f"shape of Y = {Y.shape}")
print(f"shape of Z = {Z.shape}")

ax.plot_surface(X, Y, Z, cmap=cm.coolwarm)
plt.show()


