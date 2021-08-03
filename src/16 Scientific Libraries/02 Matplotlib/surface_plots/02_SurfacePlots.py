import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

fig = plt.figure()
ax = fig.gca(projection='3d')
X = np.arange(0, 1, 0.01)
Y = np.arange(0, 1, 0.01)
X, Y = np.meshgrid(X, Y)

R = np.sqrt(X**5 + 8*X*Y**0.5)
Z = np.sin(R)

ax.plot_surface(X, Y, Z, cmap=cm.coolwarm)
plt.show()


