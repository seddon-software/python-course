'''
Create a 8x5 array of ints using the "tile" method that looks like:

    [[10 11 12 13 10]
     [11 12 13 10 11]
     [12 13 ... 
           ... 11 12]
     [13 10 11 12 13]]
'''

import numpy as np
# 
a = np.arange(10, 14)
b = np.tile(a, 10)
b = b.reshape((8,5))
print(b)
