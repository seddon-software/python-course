'''
ColorMaps
=========

Colormaps are used to enhance plots with artificial colors.  In this example we examine all the colormaps 
provided by MatPlotLib.  Of course if you really want to, you can define your own colormaps.
'''

from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d, Axes3D
import matplotlib.colors

X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)


colormaps = [eval('cm.'+s) for s in dir(cm)]

import time

fig = plt.figure("Colormaps")

for cmap in colormaps:
    try:
        if type(cmap) is not matplotlib.colors.LinearSegmentedColormap: continue
        rows = cols = position = 1
        ax = fig.add_subplot(rows, cols, position, projection='3d')
        surface = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cmap, linewidth=0, antialiased=False)
        ax.set_title(cmap.name)
        ax.set_zlim(-1.01, 1.01)
        ax.zaxis.set_major_locator(LinearLocator(10))
        ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
        fig.colorbar(surface, shrink=0.5, aspect=5)
        fig.canvas.draw()
        plt.pause(0.5)
        plt.clf()
    except Exception as e:
        print(e)