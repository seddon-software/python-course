'''
Changing Figures
================

One style of plotting allows you to switch between figures.  Here we create a figure with:
            plt.figure(1)

and then add graphs to a 3x1 grid.  The grid is created with "subplot()", and populated with sample data.  The 
signature of this function is:
            subplot(nrows, ncols, index, **kwargs)

Then we swith to a different figure:
            plt.figure(2)

and add a 2x1 grid, also populated with sample data.  Finally we switch back to the first figure and add further 
data.  You can switch back and forth between figures like this or you can decide to build each figure separately.
'''

import numpy as np
import matplotlib.pyplot as plt

t = np.arange(-2.0, 4.0, 0.01)

plt.figure(1)
plt.subplot(3,1,1)
plt.gca().patch.set_facecolor((0.1, 0.2, 0.6))
plt.plot(t, t+t**2)
plt.subplot(312)
plt.gca().patch.set_facecolor('#dd3040')
plt.plot(t, t+t**3)

# switch to figure 2
plt.figure(2)
plt.subplot(211)
plt.plot(t, t-t**2)
plt.subplot(212)
plt.plot(t, t-t**3)

# switch back to figure 1
plt.figure(1)
plt.subplot(313)
plt.gca().patch.set_facecolor('black')
plt.plot(t, t+t**4)

plt.subplots_adjust(hspace = .001)
plt.show()
