import numpy as np
from numpy import pi, cos, sin
#import matplotlib as plt
import matplotlib.pyplot as plt

import mpl_toolkits.mplot3d.axes3d as mpl

# r_[start:stop:cstep]
#     if step is an imaginary number (i.e. 100j) then its integer portion is 
#     interpreted as a number-of-points desired and the start and stop are inclusive;
#     in other words start:stop:stepj is interpreted as:
#         np.linspace(start, stop, step, endpoint=1)
# u and v are parametric variables.
u = np.r_[0:2*pi:50j] # an array from 0 to 2*pi, with 50 elements
v = np.r_[0:pi:500j]  # an array from 0 to pi, with 500 elements

x = 10 * np.outer(cos(u),sin(v))    # outer product
y = 10 * np.outer(sin(u),sin(v))
z = 10 * np.outer(np.ones(np.size(u)),cos(v))

fig = plt.figure()
ax = mpl.Axes3D(fig)
ax.plot_wireframe(x,y,z, color="black")
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
