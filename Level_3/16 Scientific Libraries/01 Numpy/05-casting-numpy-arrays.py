import numpy as np
np.set_printoptions(precision=3)

# start with a float64 array
array1 = np.fromfunction(lambda i,j: (i+2)*(j+2)**1.4, (4,4))
print(array1.dtype)
print(array1)

# casting creates a new array of int
array2 = array1.astype(int)
print(array2.dtype)
print(array2)

# casting creates a new array of bool
array3 = array1.astype(bool)
print(array3.dtype) 
print(array3)
