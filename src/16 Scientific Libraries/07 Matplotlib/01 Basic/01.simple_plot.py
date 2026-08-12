'''
Simple Plot
===========

To produce a simple plot, first create a figure with a set of axes.  Use 
            plt.subplot()

This function only returns the axes and not the figure.  If you need to know the figure use:
            figure = plt.gcf()

The plot() method takes two arrays, one for x values and one for y values.  You can also pass a number of key
word args.
'''

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt

plt.gcf().canvas.manager.set_window_title("Simple Plot")
ax = plt.subplot()      # create single figure with one axis
x = np.arange(1, 10, 0.1)
y = x**2
ax.plot(x, y, "r+")  # red plus signs
ax.set_ylabel("y = x²")
ax.set_xlabel("x")
plt.show()

