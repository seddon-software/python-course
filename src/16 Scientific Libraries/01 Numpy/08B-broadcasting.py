import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from math import sin

plt.ion()
figure = plt.figure()
ax = figure.add_subplot(1,1,1, projection='3d')
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
    plotHeights(y)

