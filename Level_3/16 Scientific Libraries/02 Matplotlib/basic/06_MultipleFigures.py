############################################################
#
#    multiple plots
#
############################################################

import numpy as np
import matplotlib.pyplot as plt

t = np.arange(-2.0, 4.0, 0.01)

plt.figure(1)
plt.subplot(311)
plt.gca().patch.set_facecolor((0.1, 0.2, 0.6))
plt.plot(t, t+t**2)
plt.subplot(312)
plt.gca().patch.set_facecolor('#dd3040')
plt.plot(t, t+t**3)

plt.figure(2)
plt.subplot(211)
plt.plot(t, t-t**2)
plt.subplot(212)
plt.plot(t, t-t**3)

plt.figure(1)
plt.subplot(313)
plt.gca().patch.set_facecolor('black')
plt.plot(t, t+t**4)

plt.subplots_adjust(hspace = .001)
plt.show()
