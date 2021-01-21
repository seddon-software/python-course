#
# The scipy.special module includes a large number of Bessel-functions
#
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import jn
fig, ax = plt.subplots()

# Bessel's equation arises when finding separable solutions to Laplace's equation and the Helmholtz
# equation in cylindrical or spherical coordinates. Bessel functions are therefore especially important 
# for many problems of wave propagation and static potentials. 
x = np.linspace(0, 10, 100)
fig.suptitle('Bessel function of first kind', fontsize=14, fontweight='bold')

for n in range(4):
    label = r"$J_{}(x)$".format(n)
    ax.plot(x, jn(n, x), label=label)
ax.legend();
plt.show()
