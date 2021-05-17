import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def zeta(s):
    x = [1/(n**s) for n in range(1, 100)]
    return sum(x)

Zeta = np.vectorize(zeta, otypes=[np.complex])

fig = plt.figure()
ax = fig.gca(projection='3d')

r = np.arange(2, 2000, 0.01)
X = [(0.5 + t*1j) for t in r]
Y = Zeta(X)
Z = [t for t in r]
# plot zeta function
ax.plot(Y.real, Y.imag, Z)

# show zeros
X0 = [0 for t in r]
Y0 = [0 for t in r]
ax.plot(X0, Y0, Z)

plt.show()


