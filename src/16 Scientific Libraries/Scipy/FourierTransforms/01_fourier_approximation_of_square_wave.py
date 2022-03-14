'''
Fourier Approximation of Square Wave
====================================

We use the formula for a square wave:

f(t) =  4 * SUM{(sin(kπt)} for 2k = 0 .. N-1 (even k only)
       ---      ---------------
        π            k

in an animation where N increases from frame to frame.  As N increases, the Fourier transformation approaches
a square wave.
'''

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from numpy import sin, pi as π



fig = plt.figure()
line, = plt.plot([], [])

def f(t, N):
    return (4*h/π) * sum([sin(k*t*ω)/k for k in np.arange(1, N, 2)])

print(4*π)
f = np.vectorize(f)
h = 1.0             # max amplitude
ω = 1.0             # frequency

def callback(frame, ω, ax):
    N = frame
    ax.set_title(f"n = {N}")
    t = np.arange(0, 20, 0.01)
    Y = f(t, N)
    line.set_data(t, Y)
    return line             # artist to be updated
 
ax = plt.gca()
ax.set_xlabel("t")
ax.set_ylabel("amplitude")
ax.set_xlim([-1.0, 20.0])
ax.set_ylim([-3.0, 3.0])
ax.set_autoscale_on(False)

anim = animation.FuncAnimation(fig, callback, fargs=(ω, ax), frames=100, interval=100)

plt.show()
