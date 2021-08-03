'''
Create a 4x6 array of random ints between 10 and 100.  Set all the even
numbers to 100.
'''

import numpy as np

a = np.random.randint(low=10, high=100, size=(4,6)); print(a)
a[a%2==0] = 100
print(a)