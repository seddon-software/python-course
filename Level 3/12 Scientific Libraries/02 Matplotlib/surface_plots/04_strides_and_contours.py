from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
from dask.array.creation import meshgrid

fig = plt.figure()
ax = fig.gca(projection='3d')

N = 8           # number of X and Y values 
STRIDE = 1      # try changing this to 2, 4 and 8
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

