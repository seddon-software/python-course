import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import time

# create a top level figure
fig = plt.figure()

# add an axes object (contains x and y axis objects)
rect=(0.25, 0.25, 0.5, 0.5)     # left, bottom, width, height
axes = fig.add_axes(rect)

# extract the axis objects
xAxis = axes.xaxis
yAxis = axes.yaxis

# add label text (normally set on the axes object)
xAxis.set_label_text('X')
yAxis.set_label_text('Y')

# add data and plot
X = np.arange(-5, 5, 0.01)
Y = X**2
axes.plot(X,Y)
plt.show()


