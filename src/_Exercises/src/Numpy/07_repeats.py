'''
Create a 6x4 array of ints between 10 and 14 where the first row is filled
with 10, the second with 11 and so on.
'''

import numpy as np

a = np.arange(10, 14)
b = np.repeat(a, 6)
b = b.reshape((4,6))
print(b)
