'''
Some Broadcasting Cases don't Work
==================================

Broadcasting in Numpy requires compatable arrays.  In this example we have a 3x4 and a 3x6 array.  Numpy doesn't
know how to expand the 3 x 4 array to make it 3 x 6.  Should it expand a to:

    [[1 2 3 4 1 1]    or    [[1 2 3 4 2 2]    or    [[1 2 3 4 3 3]    or    [[1 2 3 4 4 4]
     [1 2 3 4 1 1]           [1 2 3 4 2 2]           [1 2 3 4 3 3]           [1 2 3 4 4 4]
     [1 2 3 4 1 1]           [1 2 3 4 2 2]           [1 2 3 4 3 3]           [1 2 3 4 4 4]
     [1 2 3 4 1 1]]          [1 2 3 4 2 2]]          [1 2 3 4 3 3]]          [1 2 3 4 4 4]]

Numpy simply can't decide, so it throws a ValueError.
'''

import numpy as np
np.set_printoptions(precision=3)


a = np.array([[1,2,3,4],
              [1,2,3,4],
              [1,2,3,4]
             ])
print(a)
b = np.array([[1,2,3,4,5,6],
              [1,2,3,4,5,6],
              [1,2,3,4,5,6]
             ])
print(b)
print(f"a is {a.shape}, b is {b.shape}")
try:
    c = a + b
    print(c)
except ValueError as e:
    print(e)

