"""
A relativistic particle, B travels at 3/4 of the speed of light in the x
direction as viewed from an observer in frame of reference A.
A second relativistic particle, C  travels at 3/4 of the speed of light
in the z direction as viewed from an observer in B's frame of reference.
What is speed the of particle C as viewed from the observer in frame A.

The relativistic formulae you require can be found at:
    http://www.math.ucr.edu/home/baez/physics/Relativity/SR/velocity.html
"""

import numpy as np
import scipy.constants

np.set_printoptions(precision=3)
c = scipy.constants.c
# physical constants
print(f"speed of light = {c} m/sec")


class Point:
    def __init__(self, v, frame):
        self.frame = frame
        self.velocity = v
        
    def __add__(self, rhs):
        def γ(v):
            return 1/np.sqrt(1 - Vx*Vx/c**2)
        
        Vx, Vy, Vz = self.velocity
        Ux, Uy, Uz = rhs.velocity
        
        Wx = (Ux + Vx) / (1 + Ux*Vx/c**2)
        Wy = Uy / ((1 + Ux*Vx/c**2) * γ(Vx))
        Wz = Uz / ((1 + Ux*Vx/c**2) * γ(Vx))
        return Point(np.array([Wx, Wy, Wz]), "A")

    def abs(self):
        v = self.velocity
        return sum(v*v)**0.5

    
    
b_in_A = Point(np.array([c*.75, 0, 0]), "A")
c_in_B = Point(np.array([0, 0, c*.75]), "B")
d_in_B = Point(np.array([-c*.55, c*.57, c*.59]), "B")

c_in_A = b_in_A + c_in_B
d_in_A = b_in_A + d_in_B

print(f"Particle C when viewed in frame A (in c units):")
print(f"Velocity: {c_in_A.velocity/c}")
print(f"Speed: {c_in_A.abs()/c:.3f}")

print(f"Particle D when viewed in frame A (in c units):")
print(f"Velocity: {d_in_A.velocity/c}")
print(f"Speed: {d_in_A.abs()/c:.3f}")
