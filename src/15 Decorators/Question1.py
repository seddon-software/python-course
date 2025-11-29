'''
Vectorising
===========

Numpy allows functions to work directly with arrays.  Run the code below (it creates a simple plot).
Now define a decorator called vectorize that allows you to do the same thing without using Numpy.

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
     # define vectorize

     # decorate with vectorize
     def square(n):
          return n**2

     # decorate with vectorize
     def cube(n):
          return n**3

     # decorate with vectorize
     def quad(n):
          return n**4


     # create an array of x points without using np.linspace

     # use (uncomment) the same matplotlib code
     # ax = plt.subplot()      # create single figure with one axis
     # plt.gcf().canvas.manager.set_window_title('Your Solution')
     # plt.grid()
     # plt.plot(x, square(x), label="square")
     # plt.plot(x, cube(x), label="cube")
     # plt.plot(x, quad(x), label="quad")
     # ax.legend()
     # plt.show()

YourSolution()
