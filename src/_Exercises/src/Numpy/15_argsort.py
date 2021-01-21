'''
Create a 4x6 array of random ints between 10 and 100.  Then create
a 4x6 array of indices of representing rankings of the first array.
For example a 2x3 array
    [[49 56 61]
     [63 39 97]]
yields the rankings
    [[4 0 1]
     [2 3 5]]
'''

import numpy as np

shape = (4,6)
a = np.random.randint(low=10, high=100, size=shape); print(a)
b = np.argsort(a, axis=None).reshape(shape); print(b)
