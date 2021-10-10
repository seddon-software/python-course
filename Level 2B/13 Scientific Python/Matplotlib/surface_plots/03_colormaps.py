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

fig = plt.figure()
for cmap in colormaps:
    if type(cmap) is not matplotlib.colors.LinearSegmentedColormap: continue
    ax = Axes3D(fig)
    surface = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cmap, linewidth=0, antialiased=False)
    ax.set_title(cmap.name)
    ax.set_zlim(-1.01, 1.01)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    fig.colorbar(surface, shrink=0.5, aspect=5)
    plt.draw()
    plt.pause(0.001)
    time.sleep(0.005)
