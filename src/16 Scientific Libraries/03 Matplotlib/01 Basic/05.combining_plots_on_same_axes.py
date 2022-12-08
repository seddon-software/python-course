'''
Combining Plots
===============

You can plot several graphs on the same set of axes; here we plot 3 graphs in the axes. 
'''

import numpy as np
import matplotlib.pyplot as plt


t = np.arange(0.0, 5.0, 0.200)
redDashes = "r--"
blueSquares = "bs"
greenTriangles = "g^"

ax = plt.subplot()
ax.plot(t, t,    redDashes, 
         t, t**2, blueSquares,  
         t, t**3, greenTriangles)
ax.set_title("3 plots on One Axes")
plt.gcf().canvas.manager.set_window_title('Multiple Plots')

plt.show()

1