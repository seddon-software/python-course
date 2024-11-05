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
    
Plot the resulting orbit in 3D with matplotlib.
'''

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

k = 10.0
m = 1.0

class Particle:
    def __init__(self, name, x0, v0):
        self.name = name
        self.x = x0
        self.v = v0
    def getPosition(self):
        return self.x
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
         
p = Particle("earth", np.array([90.0, 0.0, 0.0]), np.array([0.0,0.2,0.1]))

X = []
Y = []
Z = []
for _ in range(60000):
    x, y, z = p.getPosition()
    X.append(x)
    Y.append(y)
    Z.append(z)
    p.next(0.1)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot(X, Y, Z)
ax.scatter([0], [0], [0], s=100.0, c='red', marker='o')

plt.show()


        