'''
Create a 4x6 array of random integers between 10 and 100.
Create a new 4x3 array of the lowest 50% of the original array whilst 
preserving order.
'''

import numpy as np

a = np.random.randint(low=10, high=100, size=(4,6)); print(a)
a = a[a <= np.percentile(a, 50)]
print(a.reshape((4,3)))

