import matplotlib.pyplot as plt
import numpy as np
from numpy import cos, sin, sqrt, arccos, pi as π
np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


# def cartesianToSpherical(v):
#     x, y, z = v
#     r = sqrt(x**2 + y**2 + z**2)
#     ϑ = arccos(z/r)
#     𝜑 = arccos(x/sqrt(x**2+y**2))
#     return np.array([r, ϑ, 𝜑])
# 

𝜑, ϑ = np.mgrid[0:π:250j, 0:2*π:250j]

def sphericalToCartesian(r, ϑ, 𝜑):    
    x = r * sin(𝜑) * cos(ϑ)
    y = r * sin(𝜑) * sin(ϑ)
    z = r * cos(𝜑)
    return x, y, z

fig = plt.figure()
ax = fig.gca(projection='3d')

x, y, z = sphericalToCartesian(1, ϑ, 𝜑)   
surf = ax.plot_surface(x, y, z, alpha=0.1, rstride=5, cstride=5, cmap=cm.jet,
                       linewidth=1, antialiased=False)
x, y, z = sphericalToCartesian(2, ϑ, 𝜑)   
surf = ax.plot_surface(x, y, z, alpha=0.1, rstride=5, cstride=5, cmap=cm.jet,
                       linewidth=1, antialiased=False)
ax.scatter([-2, -1, 1, 2],[0, 0, 0, 0],[0, 0, 0, 0],color="black",s=50)

ϑ = np.linspace(0, 2*π, 250)
𝜑 = arccos(2/3)
r = 2
x, y, z = sphericalToCartesian(r, ϑ, 𝜑)   
ax.plot(x, y, z)

ϑ = np.linspace(0, 2*π, 250)
𝜑 = arccos(-2/3)
r = 2
x, y, z = sphericalToCartesian(r, ϑ, 𝜑)   
ax.plot(x, y, z)

ψ = π/2 - arccos(2/3)
r = 2 * sin(ψ)
print(r, 2/3**0.5, 2*π*r)
print(6*π/5)

plt.show()

