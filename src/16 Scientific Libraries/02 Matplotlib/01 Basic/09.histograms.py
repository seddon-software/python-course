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

np.set_printoptions(precision=2, suppress=True)

import numpy as np
s = np.random.exponential(1, 1000)
print(f"{s}")
import matplotlib.pyplot as plt
bin_values, bin_edges, patches = plt.hist(s, 25)
print(f"{bin_values}")
print(f"{bin_edges}")
for rectangle in patches:
    print(rectangle)
plt.show()
