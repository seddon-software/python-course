import os; os.system("clear")
'''
In this example we take a Nexus file and smooth the data using a Savgol filter.
Note the use of Unicode variable names when setting up the smoothed plot.
    k̂wargs = {'linewidth':3, 'color':'blue'}
    ...
    plt.plot(X, Ŷ, **k̂wargs)    # smoothed plot

The Unicode variable names are not necessary, but make the code easier to read.
'''

import h5py
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter  # for smoothing

def set_title(title):
    figure = plt.gcf()
    figure.canvas.manager.set_window_title(title)

def setupAxes(xLabel, yLabel):
    set_title("MoKedge_1_15.nxs")
    ax = plt.gca()
    ax.set_facecolor((1.0, 0.9, 0.6))
    ax.set_xlabel(xLabel)
    ax.set_ylabel(yLabel)
    ax.xaxis.set_label_position("top")
    ax.yaxis.set_label_position("right")
    ax.ticklabel_format(axis='y', style='sci', scilimits=(0,5))
    plt.grid(True)

fileName = "data/MoKedge_1_15.nxs"
f = h5py.File(fileName, "r")

Y = f["/entry1/counterTimer01/It"][()]
X = f["/entry1/counterTimer01/Energy"][()]
Ŷ = savgol_filter(Y, 25, 3) # smoothing window size 25, polynomial order 3
dY = np.diff(Y)
dŶ = savgol_filter(dY, 25, 3) # smoothing window size 25, polynomial order 3

k̂wargs = {'linewidth':3, 'color':'blue'}
kwargs = {'linewidth':1, 'color':'red'}

# plot It
setupAxes('Energy', 'It')
plt.plot(X, Ŷ, **k̂wargs)    # smoothed plot
plt.plot(X, Y, **kwargs)    # original data
plt.show()

# plot d(It)
setupAxes('Energy', 'd(It)')
left = 280
right = 70
plt.plot(X[left:-right-1], dŶ[left:-right], **k̂wargs)
plt.plot(X[left:-right-1], dY[left:-right], **kwargs)
plt.show()

