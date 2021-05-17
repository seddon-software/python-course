"""
An object starts moving at from position s0 with velocity v0 and gains 
a constant acceleration of a. After time t, compute its position and
velocity.
Write a class to define the particle and provide the following methods:
    def accelerate(self, a, t):
        # dv/dt = a
        # ds/dt = v
        # v = ∫a.dt = at + s0
        # s = ∫v.dt = ∫at.dt = at^2/2 + s0.t + v0
    
    def getPosition(self):
    
    def getVelocity(self):
Perform all calculations in 3D space.  Use numpy to simplify the calculations
"""

import numpy as np


class Particle:
    def __init__(self, name, s0, v0):
        self.name = name
        self.s0 = s0
        self.v0 = v0
        
    def accelerate(self, a, t):
        # dv/dt = a
        # ds/dt = v
        # v = ∫a.dt = at + s0
        # s = ∫v.dt = ∫at.dt = at^2/2 + s0.t + v0
        self.v = a * t + self.s0
        self.s = a * t**2 + self.s0 * t + self.v0
    
    def getPosition(self):
        return self.s
    
    def getVelocity(self):
        return self.v
    
    
p1 = Particle("p1", np.array([0.5, 1.0, -0.2]), np.array([1.0, 0.3, -0.5]))
p1.accelerate(a=np.array([5.2, 2.4, 3.1]), t=10)
print(p1.getPosition(), p1.getVelocity())

