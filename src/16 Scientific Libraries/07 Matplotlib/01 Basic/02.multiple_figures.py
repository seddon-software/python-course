'''

A figure in MatPlotLib is represented by a window.  In this example we create 3 windows (figures).  The windows
will disappear unless you end with the line:
            plt.show()

see: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html
'''

import numpy as np
import matplotlib.pyplot as plt


def add_axes(fig):
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    x = np.arange(1, 10, 0.1)
    y = x**2
    ax.plot(x, y, "r+")  # red plus signs
    ax.set_ylabel("y = x²")
    ax.set_xlabel("x")
    fig.canvas.manager.set_window_title("Multiple Figures")

fig1 = plt.figure("fig.1")
fig2 = plt.figure("fig.2")
fig3 = plt.figure("fig.3")
add_axes(fig1)
add_axes(fig2)
add_axes(fig3)

plt.show()
