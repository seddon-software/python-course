from math import pi as π
from math import sin
import numpy as np
import matplotlib.pyplot as plt


def sinusoidal(t, A, ω, ϕ):
    ''' x(t)=Asin(ωt+ϕ) '''
    return A * sin(ω*t+ϕ)

sinusoidal = np.vectorize(sinusoidal)
    
t = np.arange(-10, 10, 0.01)
plt.plot(t, sinusoidal(t, A=3, ω=π/4, ϕ=π/3))
plt.grid(True)
plt.show()
    