'''
Bar Plots
=========

MatplotLib allows us to create several diiferent types of plot.  In this example we create a sample bar plot,
complete with error bars.
'''

import numpy as np
import matplotlib.pyplot as plt


N = 5
As = (20, 35, 30, 35, 27)
Bs = (25, 32, 34, 20, 25)
errorBarsA = (1, 6, 1, 6, 1)
errorBarsB = (6, 1, 6, 1, 6)
X = [0, 1, 2, 3, 4]
barWidth = 0.75

# matplotlib.pyplot.bar(x, height, width=0.8, bottom=None, *, align='center', data=None, **kwargs)[source]

p1 = plt.bar(X, As, barWidth, yerr=errorBarsA)                 # returns all the artists
p2 = plt.bar(X, Bs, barWidth, bottom=As, yerr=errorBarsB)

plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Bar Chart')
plt.xticks(X, ('G1', 'G2', 'G3', 'G4', 'G5'))
plt.yticks([0,10,20,30,40,50,60,70,80])
plt.legend((p1[0], p2[0]), ('A', 'B'))
plt.show()