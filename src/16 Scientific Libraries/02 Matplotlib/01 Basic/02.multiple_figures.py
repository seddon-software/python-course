'''

A figure in MatPlotLib is represented by a window.  In this example we create 3 windows (figures).  The windows
will disappear unless you end with the line:
            plt.show()

see: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html
'''

import numpy as np
import matplotlib.pyplot as plt


plt.figure("fig.1")
plt.figure("fig.2")
plt.figure("fig.3")
plt.show()

