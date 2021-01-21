from math import pi as π
from math import sin
import numpy as np
import matplotlib.pyplot as plt


def rectangular(t, τ):
    ''' rectangular '''
    if abs(t) <= τ/2:
        return 1
    else:
        return 0

rectangular = np.vectorize(rectangular)
    
t = np.arange(-10, 10, 0.01)
plt.plot(t, rectangular(t, τ=2.5))
plt.grid(True)
plt.show()
    