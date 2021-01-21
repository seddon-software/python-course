import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from numpy import sin, pi as π


fig = plt.figure()
line, = plt.plot([], [])

def x(n, ω, T):
    return (4/π) * sum([sin(n*ω*T)/n for n in np.arange(1, n, 2)])

x = np.vectorize(x)
ω = 1.0

def f(n, ω, ax):
    ax.set_title(f"n = {n}")
    T = np.arange(0, 20, 0.01)
    Y = x(n, ω, T)
    line.set_data(T, Y)
    return line
 
ax = plt.gca()
ax.set_xlim([-1.0, 20.0])
ax.set_ylim([-3.0, 3.0])
ax.set_autoscale_on(False)

anim = animation.FuncAnimation(fig, f, fargs=(ω, ax), frames=100, interval=100)

plt.show()
