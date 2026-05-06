'''
Subplots
========

matplotlib.pyplot.subplots() is a wrapper for matplotlib.figure.Figure.add_subplot().  The signature of this 
function is
            subplots(nrows=1, ncols=1, ...)
and returns a new figure and several axes as defined by nrows and ncols (number of rows and columns).  These
axes are normally arranged in a grid, but this can be changed (see later examples).

In this example we create a new figure with 3 rows and one column:
            fig, (ax1, ax2, ax3) = plt.subplots(3, 1)
and the figure plus a tuple of axes is returned.  We then fill the axes with some sample data.
'''

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.figure
matplotlib.figure.Figure.add_subplot

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)


fig, (ax1, ax2, ax3) = plt.subplots(3, 1)
ax1.plot(t1, f(t1), 'bo')
ax2.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
ax3.plot(t2, np.cos(2*np.pi*t2), 'r--')

plt.tight_layout()
plt.show()


