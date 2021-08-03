import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

figure = plt.figure()
ax = figure.add_subplot(1,1,1, projection='3d')


marker = "o"
 
for xs in [x for x in np.arange(10) if (x % 4) == 0]:
    for ys in np.arange(10):
        for zs in np.arange(10):
            ax.scatter(xs, ys, zs, c=(xs/10.0,ys/10.0,zs/10.0), marker=marker)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.set_xlim3d([0.0, 15.0])
ax.set_ylim3d([0.0, 15.0])
ax.set_zlim3d([0.0, 15.0])

plt.show()

