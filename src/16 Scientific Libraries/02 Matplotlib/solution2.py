'''
Write a program with a Particle class that plots the position of the particle
as it orbits a central point under the influence of an inverse square force (F).

Define a the class along the lines:
    class Particle:
        def __init__(self, name, x0, v0): ...
        def getPosition(self): ...
        def next(self, dt): ...

where x0 and v0 are the initial position and velocity of the particle.  The 
next method calculates the new position (x) and velocity (v) of the particle
a time interval dt later.

Call the next method repeatedly and use the formulae:
    dv = F * dt / m 
    dx = v * dt
to calculate the new position (x) and velocity (v) of the particle:
    v = v + dv
    x = x + dx
    
Plot the resulting orbit in 3D with matplotlib using FuncAnimation
'''

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
from functools import partial

k = 10.0
m = 2.0
SKIP = 100

class Particle:
    def __init__(self, name, x0, v0):
        self.name = name
        self.x = x0
        self.v = v0
    def getPosition(self):
        x = self.x[0]
        y = self.x[1]
        z = self.x[2]
        return ([x],[y],[z])
    def next(self, dt):
        x = self.x[0]
        y = self.x[1]
        z = self.x[2]
        R = (x**2 + y**2 + z**2)**0.5
        Rhat = np.array([x, y, z])/R
        F = -k * Rhat / R**2
        # F = m * dv/dt
        dv = F * dt / m
        self.v += dv
        # dx/dt = v
        self.x += self.v * dt
         
earth = Particle("earth", np.array([0.0, 0.0, 0.0]), np.array([0.0,0.0,0.0]))
satellite1 = Particle("satellite1", np.array([45.0, 0.0, 0.0]), np.array([0.0,0.3,0.1]))
satellite2 = Particle("satellite2", np.array([90.0, 0.0, 0.0]), np.array([0.0,0.2,-0.1]))

def update_plot(ax, sc2, sc3, frame):
    for n in range(SKIP):
        satellite1.next(0.1)
        satellite2.next(0.1)
    sc2._offsets3d = satellite1.getPosition()
    sc3._offsets3d = satellite2.getPosition()

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_xlim3d([-100.0, 100.0])
ax.set_ylim3d([-100.0, 100.0])
ax.set_zlim3d([-100.0, 100.0])

sc1 = ax.scatter(*earth.getPosition(), s=100.0, c='red', marker='o')
sc2 = ax.scatter(*satellite1.getPosition(), s=25.0, c='blue', marker='o')
sc3 = ax.scatter(*satellite2.getPosition(), s=10.0, c='green', marker='o')

pfn = partial(update_plot, ax, sc2, sc3)
ani = FuncAnimation(fig, func=pfn, frames=1000, interval=100)
plt.show()



        