'''
Find the intersection of two 1D arrays
'''

import numpy as np

a = np.array([5,6,1,5,0,4,6,10,11,2,3])
b = np.array([6,2,10,9,4,9,3,2,1])

print(np.intersect1d(a,b))
