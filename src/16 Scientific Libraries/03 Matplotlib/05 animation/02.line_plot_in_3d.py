'''
Animation of a Line in 3D
=========================

This similar to the previous examples, but with a few changes.

1) this time we have an initialization function "init()" which is called to set to scene prior to the first
frame.  This draws a red circle at the origin.

2) animate produces an array t that has shape (300,) using:
            t = np.arange(i*dt, i*dt+3, dt)
The array is used to parameterize the x, y and z arrays. These arrays will also have shape (300,).  That means the
line will consist of 300 points.  Since t varies on each frame the x, y, z arrays will also change, giving the 
impression of the line moving.

3) To feed x, y and z into the actual line artist we use:
            line.set_data(x, y)
            line.set_3d_properties(z)
The second line is required to set the z component of the line (because line was originally designed for 2D use 
and "set_data()" was never updated for the 3D case).

4) the return from "animation.FuncAnimation()" is used solely to keep a reference to the animation object.  
If you don't store the return, the animation object will get garbage collected and the animation will end
prematurely.
'''

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
fig.canvas.manager.set_window_title("3D Curve Animation")
ax = fig.add_subplot(111, projection='3d')

# initial view
elevation = 10
viewing_angle = 125
ax.view_init(elev=elevation, azim=viewing_angle)

# set the coordinates for the line as empty and fill in data after animate() called.
line, = ax.plot([], [], [], lw=2)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_xlim3d([-1.0, 200.0])
ax.set_ylim3d([-1.0, 2000.0])
ax.set_zlim3d([-1.0, 10.0])
ax.set_autoscale_on(False)

dt = 0.01

def init():
    ax.plot([0], [0], [0], 'ro')

def animate(i):
    t = np.arange(i*dt, i*dt+3, dt)
    x = 2*t**3+1
    y = 2*t**2
    z = t
    # there is no set_data for 3D, so you have to do it this way
    line.set_data(x, y)
    line.set_3d_properties(z)
    return line        # the artist to be updated

# create animation object
# note anim keeps a reference to the FuncAnimation object
# without which the animation dies premeturely
animinmationObject = animation.FuncAnimation(fig, animate, init_func=init, frames=650, interval=50)

plt.show()




