'''
Histograms
==========

Histograms are fairly easy to use with
            count, bins, ignored = plt.hist(s, 25)

The return values are
            count           : values in each of the bins
            bins            : x coord of the LHS of bin
            ignored         : lots of related information (ignored is a misnomer)
'''

import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(precision=2, suppress=True)

import numpy as np
s = np.random.exponential(1, 1000)
print(f"{s}")
import matplotlib.pyplot as plt
count, bins, ignored = plt.hist(s, 25)
print(count)
print(f"{bins}")
print(ignored)
plt.show()
