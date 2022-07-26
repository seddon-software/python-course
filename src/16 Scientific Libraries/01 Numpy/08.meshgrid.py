'''
Meshgrid
========
Here we look at the meshgrid function, often used in conjunction with surface plots in matplotlib.  We will need
surface plots to explain broadcasting in subsequent examples.

Matplotlib supports surface plots.  However, you need to prepare your data before plotting.  The plot_surface()
method takes 3 numpy arrays; each array has to be 2 dimensional and all arrays must be the same size.

In this example we start with 100 x and 100 y points stored in the X and Y arrays.  However these arrays are 1
dimensional and represent points on the x and y axes.  These arrays need to be projected onto the z=0 plane
to convert them into 2 dimensional arrays before plotting.  The meshgrid() function performs this projection.

After projection the X array contains the x values for every point in the z=0 plane that we are plotting.  The 
same goes for the Y array.

To give you an idea of what meshgrid() does these would be the X and Y arrays if we used
            X = np.arange(0, 0.1, 0.01)
            Y = np.arange(0, 0.1, 0.01)
            X, Y = np.meshgrid(X, Y)

where the grid would be 10 x 10 points.

X = [[0.   0.01 0.02 0.03 0.04 0.05 0.06 0.07 0.08 0.09]
    [0.   0.01 0.02 0.03 0.04 0.05 0.06 0.07 0.08 0.09]
    [0.   0.01 0.02 0.03 0.04 0.05 0.06 0.07 0.08 0.09]
    [0.   0.01 0.02 0.03 0.04 0.05 0.06 0.07 0.08 0.09]
    [0.   0.01 0.02 0.03 0.04 0.05 0.06 0.07 0.08 0.09]
    [0.   0.01 0.02 0.03 0.04 0.05 0.06 0.07 0.08 0.09]
    [0.   0.01 0.02 0.03 0.04 0.05 0.06 0.07 0.08 0.09]
    [0.   0.01 0.02 0.03 0.04 0.05 0.06 0.07 0.08 0.09]
    [0.   0.01 0.02 0.03 0.04 0.05 0.06 0.07 0.08 0.09]
    [0.   0.01 0.02 0.03 0.04 0.05 0.06 0.07 0.08 0.09]]

Y = [[0.   0.   0.   0.   0.   0.   0.   0.   0.   0.  ]
    [0.01 0.01 0.01 0.01 0.01 0.01 0.01 0.01 0.01 0.01]
    [0.02 0.02 0.02 0.02 0.02 0.02 0.02 0.02 0.02 0.02]
    [0.03 0.03 0.03 0.03 0.03 0.03 0.03 0.03 0.03 0.03]
    [0.04 0.04 0.04 0.04 0.04 0.04 0.04 0.04 0.04 0.04]
    [0.05 0.05 0.05 0.05 0.05 0.05 0.05 0.05 0.05 0.05]
    [0.06 0.06 0.06 0.06 0.06 0.06 0.06 0.06 0.06 0.06]
    [0.07 0.07 0.07 0.07 0.07 0.07 0.07 0.07 0.07 0.07]
    [0.08 0.08 0.08 0.08 0.08 0.08 0.08 0.08 0.08 0.08]
    [0.09 0.09 0.09 0.09 0.09 0.09 0.09 0.09 0.09 0.09]]

In our example we are actually working with a larger grid (100 x 100).  The Z array is calculated in the normal 
way (element by element).  

Finally we use a color map to make the plot attractive. 

Note:
1. This exapmple is repeated in the MatPlotLib chapter
2. We are getting an error with Anaconda to with mixing versions of libstdc++.  This doesn't seem to affect 
the result.
'''

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

fig = plt.figure()
ax = fig.gca(projection='3d')
X = np.arange(0, 1, 0.01)
Y = np.arange(0, 1, 0.01)
X, Y = np.meshgrid(X, Y)
print(Y)
R = np.sqrt(X**5 + 8*X*Y**0.5)
Z = np.sin(R)

ax.plot_surface(X, Y, Z, cmap=cm.coolwarm)
plt.show()


