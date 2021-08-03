'''
Perform a Cartesian to Spherical coordinate transformation on each of
the Cartesian unit vectors:
    iHat = [1, 0, 0]
    jHat = [0, 1, 0]
    kHat = [0, 0, 1]
Note that the transfomation for kHat causes a singularity in Spherical 
coordinates, so try vectors very near kHat instead:
    kHat_plus  = [+0.0001,0,1])
    kHat_minus = [-0.0001,0,1])
'''
import numpy as np
from numpy import sqrt, arccos
np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})


def cartesianToSpherical(v):
    x, y, z = v
    r = sqrt(x**2 + y**2 + z**2)
    ϑ = arccos(z/r)
    𝜑 = arccos(x/sqrt(x**2+y**2))
    return np.array([r, ϑ, 𝜑])


iHat = np.array([1,0,0])
jHat = np.array([0,1,0])
kHat_plus  = np.array([+0.0001,0,1])
kHat_minus = np.array([-0.0001,0,1])
print( f"unit iHat = {cartesianToSpherical(iHat)}" )
print( f"unit jHat = {cartesianToSpherical(jHat)}" )
print( f"unit kHat+ = {cartesianToSpherical(kHat_plus)}" )
print( f"unit kHat- = {cartesianToSpherical(kHat_minus)}" )
