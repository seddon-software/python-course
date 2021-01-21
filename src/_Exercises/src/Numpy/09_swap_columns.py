'''
Create a 4x6 array of ints.  Swap columns 2 and 4.
'''

import numpy as np

a = np.arange(100,124).reshape(4,6)
print(a)

a[:,(2,4)] = a[:,(4,2)]
print(a)
