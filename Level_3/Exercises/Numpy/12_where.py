'''
Create two 1D int arrays of equal size.  Create a new array of the
same size, selecting elements from the first array when the element
in this array is even, and selecting elements from the second array 
when the element in the first array is odd.
'''
import numpy as np

a = np.arange(10,50,3)
b = np.arange(100,114)

difference = np.where(a%2, a, b)
print(difference)
