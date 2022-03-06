'''
Animation of a Shape in 3D
==========================

MatPlotLib supports animation using the function:
            ani = FuncAnimation(fig, update_plot, frames=frames, fargs=(data,sc), interval=100)

This does not provide sophisticated animation as in games, but is intended to add a timing element to plotting.
The key part of this call is the second parameter:
            update_plot
which specifies a function pointer; the function will be called repeatedly during the animation.  The update will 
be performed every 100 msec and frames will indicate the number of frame in the animation.  When update_plot
is called, the frame number will be passed as a monotonically increasing number, starting at 1.  If you look at
the function def statement:
            def update_plot(frame, data, sc):
you will notice two more parameters are passed to update_plot.  These parameters were specified in the "fargs"
tuple of FuncAnimation.  In this example we calculate all our animation data prior to calling FuncAnimation, 
but this is not required.

Other points of interest are:
1)          matplotlib.use('TkAgg')
This defines the backend graphics driver used by MatPlotLib.  "backend" does all the hard work behind the scenes
to make draw the figure. There are two types of backends: user interface backends (for use in PyQt/PySide, 
PyGObject, Tkinter, wxPython, or macOS/Cocoa); also referred to as "interactive backends") and hardcopy backends 
to make image files (PNG, SVG, PDF, PS; also referred to as "non-interactive backends").  You can list the 
available backends with:
            print(matplotlib.rcsetup.interactive_bk)
            print(matplotlib.rcsetup.non_interactive_bk)
            print(matplotlib.rcsetup.all_backends)
Several of the backends will not work with this example.

2) inserting a breakpoint in the code will likely cause a change of backend and the code will fail.  So run this 
code without breakpoints.

3)  The return from update_frame tells the animation which "artist" to update, in this case our 3D axes (ax).  
Note this function is very short but does update
            sc._offsets3d
which is a poorly documented feature, but should contain the x, y, z coordinates of objects in the scatter plot.
'''

import numpy as np
from numpy import array, dot
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
from matplotlib.animation import FuncAnimation
from math import sqrt

def update_plot(frame, data, sc):
    sc._offsets3d = data[frame]
    return sc

def main():
    matplotlib.use('TkAgg')
    frames = 2000
    dimensions = 3
    particles = 20
    data = np.ones(frames * dimensions * particles)
    data = data.reshape(frames, dimensions, particles)

    for particle in range(particles):
        for dimension in [0, 1, 2]:
            for frame in range(frames): 
                # build some snake like movement for the points
                if dimension == 0: data[frame][dimension][particle] = particle * np.sin(frame/40.0) * 10 * np.sin(particle/4.0)
                if dimension == 1: data[frame][dimension][particle] = particle * np.sin(frame/20.0) * 10
                if dimension == 2: data[frame][dimension][particle] = particle * np.cos(frame/10.0) * 10
                
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1, projection='3d')
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_xlim3d([-250.0, 250.0])
    ax.set_ylim3d([-250.0, 250.0])
    ax.set_zlim3d([-250.0, 250.0])
    ax.set_autoscale_on(False)

    ix, iy, iz = data[0]
    sc = ax.scatter(ix, iy, iz, s=100.0, c='red', marker='d')

    ani = FuncAnimation(fig, update_plot, frames=frames, fargs=(data,sc), interval=100)
    plt.show()


main()
    