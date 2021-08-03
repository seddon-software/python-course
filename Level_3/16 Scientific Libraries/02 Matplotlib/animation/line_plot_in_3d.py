from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np



fig = plt.figure()
ax = fig.gca(projection="3d")

elevation = 10
viewing_angle = 125

ax.view_init(elev=elevation, azim=viewing_angle)
line, = ax.plot([], [], [], lw=2)
line2, = ax.plot([], [], [], 'ro')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_xlim3d([-1.0, 200.0])
ax.set_ylim3d([-1.0, 2000.0])
ax.set_zlim3d([-1.0, 10.0])
ax.set_autoscale_on(False)

dt = 0.01

def init():
    line2.set_data(0, 0)
    line2.set_3d_properties(0)
    return line2

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
animinmationObject = animation.FuncAnimation(fig, animate, init_func=init, \
                                             frames=650, interval=50)

plt.gcf().canvas.set_window_title("3D Curve Animation")
plt.show()










