############################################################
#
#    broadcasting
#
############################################################

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

f = y * np.cos(x)
# f = x * y
print(f)
fig = plt.figure()
ax = Axes3D(fig)
surface = ax.plot_surface(x, y, f, cmap="terrain", rstride = 25, cstride = 5) #, rstride=1, cstride=1, cmap=cmap, linewidth=0, antialiased=False)
plt.show()
1
