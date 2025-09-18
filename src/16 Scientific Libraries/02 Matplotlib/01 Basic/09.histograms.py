'''
Histograms
==========

Histograms are fairly easy to use with
            count, bins, ignored = plt.hist(s, 25)

The return values are
            count           : values in each of the bins
            bins            : x coords of the left hand edges of the bins
            patches         : information on bin rectangles

see:
    https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html?highlight=hist#matplotlib.pyplot.hist
'''

import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(precision=2, suppress=True, formatter={'float_kind': lambda x: f"{x:0.2f}"})

# draw samples from an exponential distribution.
samples = np.random.exponential(1, 1000)

print(f"min value = {min(samples):0.3f}")
print(f"max value = {max(samples):0.3f}")
import matplotlib.pyplot as plt
plt.hist(samples, bins=30, edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Exponential Distribution Samples')
plt.show()

