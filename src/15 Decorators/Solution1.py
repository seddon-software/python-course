'''
Vectorising
===========

Numpy has a vectorize function to allow scaler functions work with arrays.  Create a decorator
called vectorise to do the same thing. 
'''

import numpy as np
import matplotlib.pyplot as plt

def NumpySolution():
     def square(n):
          return n**2

     def cube(n):
          return n**3

     def quad(n):
          return n**4

     x = np.linspace(-3, 3, 100)
     y = cube(x)

     ax = plt.subplot()      # create single figure with one axis
     plt.gcf().canvas.manager.set_window_title('Numpy Solution')
     plt.grid()
     plt.plot(x, square(x), label="square")
     plt.plot(x, cube(x), label="cube")
     plt.plot(x, quad(x), label="quad")
     ax.legend()
     plt.show()

NumpySolution()

def YourSolution():
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

     x = [n/100 for n in range(-300, 300)]
     y = cube(x)
     ax = plt.subplot()      # create single figure with one axis
     plt.gcf().canvas.manager.set_window_title('Your Solution')
     plt.grid()
     plt.plot(x, square(x), label="square")
     plt.plot(x, cube(x), label="cube")
     plt.plot(x, quad(x), label="quad")
     ax.legend()
     plt.show()

YourSolution()
