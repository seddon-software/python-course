'''
Scatter Plots
=============

Scatter plots draw glyphs at each xy point.

see:
    https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html
'''

import numpy as np
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(1, 2)
fig.canvas.manager.set_window_title("Scatter Plots")

# Left hand side plot
ax1.scatter([1,2,3,4,5], [1,2,3,5,8], c='green')  # green dots
ax1.set_title('Scatterplot green dots')  
ax1.set_xlabel('x'); 
ax1.set_ylabel('y')


# Right hand side plot
ax2.scatter([1,2,3,4,5], [8,13,21,34,55], c='blue')  # blue stars
ax2.set_title('Scatterplot blue stars')  
ax2.set_xlabel('x')
ax2.set_ylabel('y')

plt.show()
