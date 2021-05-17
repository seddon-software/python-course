import matplotlib.pyplot as plt
import numpy as np
from numpy import sin, cos, pi as π
import scipy.integrate as integrate

def stairFunction(t):
    x = t % 6
    if x > 5: return 5
    if x > 4: return 4
    if x > 3: return 3
    if x > 2: return 2
    if x > 1: return 1
    return 0

stairFunction = np.vectorize(stairFunction)


T = 6.0
max = 50
f = stairFunction

a = np.empty((max+1))
b = np.empty((max+1))

a[0] = (1/T) * integrate.quad(lambda t:f(t), 0, T)[0]
for m in range(1, max):
    a[m] = (2/T) * integrate.quad(lambda t:f(t)*cos(2*π*m*t/T), 0, T)[0]
    b[m] = (2/T) * integrate.quad(lambda t:f(t)*sin(2*π*m*t/T), 0, T)[0]

def g(t):
    result = a[0]
    for m in range(1, max):
        result += a[m]*cos(2*π*m*t/T) + b[m]*sin(2*π*m*t/T)
    return result
g = np.vectorize(g)

t = np.arange(0, 13, 0.1)

plt.plot(t, f(t))
plt.plot(t, g(t))
plt.show()
