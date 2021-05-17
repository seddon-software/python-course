'''
Create a 4x6 array of random ints between 10 and 100.  Create a new 1D array
with all the numbers in the first array that are less than 50.
'''

import numpy as np

a = np.random.randint(low=10, high=100, size=(4,6)); print(a)
b = a[a[:] < 50]
print(b)