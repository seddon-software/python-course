############################################################
#
#    subplots
#
############################################################

import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)


fig, (ax1, ax2, ax3) = plt.subplots(3, 1)
ax1.plot(t1, f(t1), 'bo')
ax2.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
ax3.plot(t2, np.cos(2*np.pi*t2), 'r--')

plt.tight_layout()
plt.show()

1