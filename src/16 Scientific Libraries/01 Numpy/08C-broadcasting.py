'''
More Broadcasting
=================

Here is the same example, but with many more points.  The x and y arrays have 800 values and the z=0 plane will
therefore have 800x800=640000 points at which we calculate our formula.  I've changed the formula this time to 
create a more interesting surface:
            z = y * np.cos(x)
'''

import numpy as np
import matplotlib
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d, Axes3D

# a = [2, 4, 6, 8, 10]
a = np.arange(2, 10, 0.01)
x = np.hstack(a); print(x)
y = np.vstack(a); print(y)

z = y * np.cos(x)
print(z)
fig = plt.figure()
ax = Axes3D(fig)
surface = ax.plot_surface(x, y, z, cmap="terrain", rstride = 25, cstride = 5) #, rstride=1, cstride=1, cmap=cmap, linewidth=0, antialiased=False)
plt.show()
1
