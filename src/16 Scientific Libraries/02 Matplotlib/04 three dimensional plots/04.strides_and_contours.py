'''
Strides and Contours
====================

Strides define the length of tessellations on a surface plot.  You can define row strides and column strides
independently as in:
            STRIDE = 1
            ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, rstride=STRIDE, cstride=STRIDE, alpha=0.8)

If you try rerunning the example with other values of STRIDE you will quickly get the idea.  The lower the stride, 
the more tessellations.  In this example we are only using 8x8 arrays (N=8), so the output is granular.  If you 
increase N to, say 100, you can investigate the granulation of the tessellations by low (STRIDE=1) and high 
values of STRIDE (STRIDE=25).

Contours are a projection of the surface plot onto the z=0 plane.

We look at both strides and contours in this example.
'''

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
from dask.array.creation import meshgrid

fig = plt.figure()
ax = fig.gca(projection='3d')

N = 8           # number of X and Y values 
STRIDE = 1     # try changing this to 2, 4 and 8
X = np.arange(5, 5+N+1)
Y = np.arange(5, 5+N+1)
X,Y = np.meshgrid(X, Y)
Z = X*Y + 10

# rstride and cstride define width of bands of color
ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, rstride=STRIDE, cstride=STRIDE, alpha=0.8)

# also show a contour map
cset = ax.contourf(X, Y, Z, zdir='z', offset=5, cmap=cm.coolwarm)  # @UndefinedVariable

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()

