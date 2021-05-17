from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np



fig = plt.figure()
fig.canvas.set_window_title("Planetary Orbits")
ax = fig.gca(projection="3d")
ax.set_title("Satellite Tracing Orbiting Earth")

elevation = 75
viewing_angle = 125
ax.view_init(elev=elevation, azim=viewing_angle)

earth, = ax.plot([0], [0], [0], 'bo')
orbit, = ax.plot([], [], [], lw=1, color='green', marker='o', markersize=1)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_xlim3d([-100.0, 100.0])
ax.set_ylim3d([-100.0, 100.0])
ax.set_zlim3d([-100.0, 100.0])

k = 10.0
m = 1.0

class Particle:
    history_size = 250
    def __init__(self, name, x, v):
        self.history_buffer = np.empty((0,3))
        self.name = name
        self.x = x
        self.v = v
        self.index = 0
        self.history_buffer = np.append(self.history_buffer, [self.x], axis=0)

    def getPosition(self):
        return self.x
    
    def next(self, dt):
        # F = m * dv/dt  => dv = F * dt / m
        # dx/dt = v      => dx = v * dt => x = x + dx 
        #                                    = x + v * dt
        x = self.x[0]
        y = self.x[1]
        z = self.x[2]
        R = (x**2 + y**2 + z**2)**0.5
        Rhat = np.array([x, y, z])/R
        F = -k * Rhat / R**2
        dv = F * dt / m
        self.v += dv
        self.x += self.v * dt
        self.index += 1
        if self.index >= Particle.history_size:
            self.history_buffer[self.index % Particle.history_size] = self.x
        else:
            self.history_buffer = np.append(self.history_buffer, [self.x], axis=0)

    def history(self):
        n = self.index % Particle.history_size
        return np.roll(self.history_buffer,-n-1, axis=0)

x0 = np.array([90.0, 0.0, 0.0])
v0 = np.array([0.1,0.2,0.1])
p = Particle("earth", x0, v0)

def init():
    earth.set_data(0, 0)
    earth.set_3d_properties(0)
    return earth

def animate(frameNo):
    p.next(dt=2)       
    h = p.history().T   # must transpose buffer to extract X,Y and Z
    X, Y, Z = h[0], h[1], h[2]
    X = np.append(X, [0.0])
    Y = np.append(Y, [0.0])
    Z = np.append(Z, [0.0])
    orbit.set_data(X, Y)
    orbit.set_3d_properties(Z)
    return orbit        # the artist to be updated
    

a = animation.FuncAnimation(fig, animate, init_func=init, frames=100000, \
                               interval=50)

plt.show()










