import numpy as np
np.set_printoptions(precision=3)

# this only wors for scalars
def square(x): return x * x

# vectorize function to return floats
square = np.vectorize(square, otypes=[np.float])
x = range(5, 10)
print(square(x))         # now works for vectors
print(square(10))        # but still works for scalars

