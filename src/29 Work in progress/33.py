'''
11 Introduction to Functional: some parts not covered

spreadsheets
scikitimage
14 Testing
15 Threading and Concurrency
'''

import numpy as np
from numpy import sin, cos, pi as π
import matplotlib.pyplot as plt

m = 1
t = 0
x = 9.9
v = -0.45
dt = 0.01
X = []
T = []

def force(x,v):
    return sin(2*π*x)*v/x**2
    
for n in np.arange(0, 100, 0.01):
    t = t + dt
    F = force(x,v)
    dv = F*dt/m
    v = v + dv
    dx = v * dt
    x = x + dx
    if x < 0: break
    print(f"{t:.2f} {v:.2f} {x:.2f}")
    X.append(x)
    T.append(t)
    
plt.plot(T, X)
plt.grid()
plt.show()

