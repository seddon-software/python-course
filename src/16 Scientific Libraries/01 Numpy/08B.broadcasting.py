'''
This example is intended to be used in the debugger.  Note we are using interactive mode:
            plt.ion()

Put a breakpoint on the line:
            plotHeights(y)

Then as you step through this example you will notice the product of the  x and y coordinates are plotted for
a grid of points on the z=0 plane.  
        ax.plot([x,x],[y,y],[0,x*y])

The height (z=x*y) is illustrated row by row.  As the rows unfold, you can see we are forming a surface plot.
Calculations like this are the reason Numpy uses element by element calculations in expressions involving 
multi-dimemsional arrays.
'''

import numpy as np
import time
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from math import sin

plt.ion()
figure = plt.figure()
ax = Axes3D(figure, auto_add_to_figure=False)
figure.add_axes(ax)
ax.view_init(elev=20.0, azim=105.0)

plt.rcParams['lines.linewidth'] = 4
marker = "o"
MIN = 1
MAX = 8

ax.set_xlim3d([MIN, MAX])
ax.set_ylim3d([MIN, MAX])
ax.set_zlim3d([0.0, MAX**2])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
for xs in np.arange(MIN, MAX):
    for ys in np.arange(MIN, MAX):
        for zs in [0]*MAX:
            ax.scatter(xs, ys, zs, c="blue", marker=marker)

def plotHeights(y):
    for x in range(MIN, MAX):
        ax.plot([x,x],[y,y],[0,x*y])

for y in range(MIN, MAX):
    # put breakpoint in here
    plotHeights(y)
    input(">")

plt.ioff()
plt.show()
