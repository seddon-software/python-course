'''
Create a 4x6 array of random integers between 10 and 100.
Set the lowest 50% of the array to 0.
'''

import numpy as np

a = np.random.randint(low=10, high=100, size=(4,6)); print(a)
a[a <= np.percentile(a, 50)] = 0
print(a)

