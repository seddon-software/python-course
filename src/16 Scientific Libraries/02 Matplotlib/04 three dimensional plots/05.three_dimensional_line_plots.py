'''
3D Line Plots
=============

In addition to surface plots, you can produce line plots in 3 dimensional space.  This example is based on a
parametrized curved using the variable t.  As t varies, x, y and z will change.
'''

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
t = np.arange(0, 10, 0.01)
z = t
x = 2*t**3+1
y = 2*t**2

# x, y and z are 1D arrays
ax.plot(x, y, z, label='parametric curve')
ax.legend()

plt.show()
