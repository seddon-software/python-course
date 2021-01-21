'''
Create a 3x10 array.  Rotate the array by 90 degrees, 4 times, so you get back
to the original array.
'''
import numpy as np

a = np.arange(10, 40).reshape(3, 10)

a = np.rot90(a); print(a); print()
a = np.rot90(a); print(a); print()
a = np.rot90(a); print(a); print()
a = np.rot90(a); print(a); print()

