'''
Surface Plots
=============

This is the same example, except we generate the X and Y arrays with
            X = np.arange(0, 1, 0.01)
            Y = np.arange(0, 1, 0.01)
            X, Y = np.meshgrid(X, Y)
The magic is performed by meshgrid() which takes two 1D arrays and returns two 2D arrays of the form shown
in the previous example.  Note that this time we are creating 100x100 arrays (for a much more fine grained 
result).
'''

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
X = np.arange(0, 1, 0.01)
Y = np.arange(0, 1, 0.01)
X, Y = np.meshgrid(X, Y)

R = np.sqrt(X**5 + 8*X*Y**0.5)
Z = np.sin(R)
print(f"shape of X = {X.shape}")
print(f"shape of Y = {Y.shape}")
print(f"shape of Z = {Z.shape}")

ax.plot_surface(X, Y, Z, cmap=cm.coolwarm)
plt.show()


