'''
Multiple Figures and Axes
=========================

This example shows how to create multiple figures (windows), each with 4 sets of axes (with various color
bacgrounds).  Note the use of
            fig.set_tight_layout(True)
to avoid axes overlapping.
'''

import numpy as np
import matplotlib.pyplot as plt


colors = ["yellow", "red", "blue", "green"]
fig3 = plt.figure("fig.3")
fig2 = plt.figure("fig.2")
fig1 = plt.figure("fig.1")
print(f"type of Figure: {type(fig1)}")

for fig in [fig1, fig2, fig3]:
    fig.set_tight_layout(True)
    for n in range(1, 5):
               # add_subplot(nrows, ncols, index, **kwargs)
        ax = fig.add_subplot(2, 2, n, title=f"axes-{n}")
        ax.set_facecolor(colors[n-1])

print(f"type of Axes: {type(ax)}")
plt.tight_layout()
plt.show()

