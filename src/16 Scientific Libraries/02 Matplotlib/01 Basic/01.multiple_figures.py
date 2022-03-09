'''
Multiple Figures
================

A figure in MatPlotLib is represented by a window.  In this example we create 3 windows (figures).  The windows
will disappear unless you end with the line:
            plt.show()
'''

import numpy as np
import matplotlib.pyplot as plt


plt.figure("fig.1")
plt.figure("fig.2")
plt.figure("fig.3")
plt.show()

