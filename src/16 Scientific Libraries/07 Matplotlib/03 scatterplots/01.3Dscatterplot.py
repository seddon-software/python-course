'''
3D Scatter Plots
================

Here we show a 3D scatter plot.  I've arranged to create 3 planes of 100 markers.  The planes defined by the
x value are restricted to x = 0, 4 and 8:
            for xs in [x for x in np.arange(10) if (x % 4) == 0]:

To make the plot more interesting I've varied the colors of the markers, dependent on the x, y, z coords:
            c=(xs/10.0,ys/10.0,zs/10.0)
'''

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

figure = plt.figure("3D Scatter Plot")
ax = figure.add_subplot(1,1,1, projection='3d')


marker = "o"

for xs in [x for x in np.arange(10) if (x % 4) == 0]:
    for ys in np.arange(10):
        for zs in np.arange(10):
            ax.scatter(xs, ys, zs, color=(xs/10.0,ys/10.0,zs/10.0), marker=marker)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_xlim3d([0.0, 15.0])
ax.set_ylim3d([0.0, 15.0])
ax.set_zlim3d([0.0, 15.0])

plt.show()

