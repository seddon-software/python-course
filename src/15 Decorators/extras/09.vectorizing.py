'''
Vectorising
===========

Numpy has a vectorize function to allow scaler functions work with arrays.  We can provide a convenient decorator
to do the same thing. 
'''

import numpy as np
import matplotlib.pyplot as plt

def vectorize(fn):
    def convert(args):
        return [fn(arg) for arg in args]
    return convert

@vectorize
def square(n):
    return n**2

@vectorize
def cube(n):
    return n**3

@vectorize
def quad(n):
    return n**4

x = np.linspace(-3, 3, 100)
y = cube(x)

plt.gca().set_title("vectorize decorator")
plt.grid()
plt.plot(x, y)
plt.show()


