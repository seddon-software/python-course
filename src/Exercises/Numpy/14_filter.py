'''
Create a 4x6 array of random ints between 10 and 100.
Filter this array and produce a 1D array of the numbers divisible by 3.
'''
import numpy as np

a = np.random.randint(low=10, high=100, size=(4,6))
b = a[a % 3 == 0]
print(f"a = {a}")
print(f"b = {b}")

 