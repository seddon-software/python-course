'''
Create a 4x6 array of random ints between 10 and 100.
Look up what it means to define a masked array and then create
a masked array where all values in the original array that are
less than 50 are masked out.
'''

import numpy as np
import numpy.ma as ma

a = np.random.randint(low=0, high=100, size=(4,6)); print(a)
mask = ma.masked_array(a, mask=a<=50)

print(mask)
