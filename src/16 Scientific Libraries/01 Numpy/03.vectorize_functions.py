'''
Vectorize
=========

Numpy works with multi-dimensional data (vectors) rather than scalers.  However we may want to work with an 
existing function that only takes scaler input.  If we try passing a list to such a function it fails.  To 
overcome this, Numpy provides a "vectorize" function.  

This will allow us to pass vectors to our function whilst still allowing it to work with scalers.
'''

import numpy as np
np.set_printoptions(precision=3)

# this only works for scalars
def square(x): return x * x

# vectorize function to return floats
square = np.vectorize(square, otypes=[np.float])
x = range(5, 10)
print(square(x))         # now works for vectors
print(square(10))        # but still works for scalars

