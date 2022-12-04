import h5py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from math import log, sqrt
from scipy.optimize import curve_fit

def quadratic(x, a, b, c):
    return a*x**2 + b*x + c

def main():    
    plt.gcf().canvas.manager.set_window_title("Curve Fitting")
    ax = plt.gca()
    ax.set_title("quadratic")
    x = np.arange(-4, 4, 0.01)
    noise = np.random.rand((len(x)))-0.5 # between -0.5 and 0.5
    y = 7.8*x**2 - 2.3*x + 13.4 + 50 * noise
    def initialGuess():    
        a = 5
        b = 0
        c = 8
        return [a, b, c]
    
    fit, estimated_covariance = curve_fit(quadratic, x, y, p0=initialGuess())
    print(fit)
    plt.plot(x, y)
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    plt.plot(x, quadratic(x, *fit), 'r-',
             label=f'a={fit[0]:.2f} b={fit[1]:.2f} c={fit[2]:.2f}')
    plt.legend()
    plt.show()


main()

