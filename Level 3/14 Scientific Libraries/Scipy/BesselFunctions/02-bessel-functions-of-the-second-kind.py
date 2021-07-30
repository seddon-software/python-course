#
# The scipy.special module includes a large number of Bessel-functions
#
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import kn
fig, ax = plt.subplots()

# Bessel's equation arises when finding separable solutions to Laplace's equation and the Helmholtz
# equation in cylindrical or spherical coordinates. Bessel functions are therefore especially important 
# for many problems of wave propagation and static potentials. 
x = np.linspace(0.2, 5, 100)
fig.suptitle('Modified Bessel function of second kind', fontsize=14, fontweight='bold')

plt.ylim((0, 10))

for n in range(4):
    label = r"$K_{}(x)$".format(n)
    ax.plot(x, kn(n, x), label=label)
ax.legend();
plt.show()

