import h5py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from math import log, sqrt
from scipy.optimize import curve_fit

def gauss(x, peak, μ, σ):
    return peak*np.exp(-(x-μ)**2/(2.*σ**2))

def main():
    fileName = "data/14763.dat"
    data = pd.read_csv(fileName, 
                       skiprows = 6,
                       engine = 'python',
                       sep = '[ \t]+')
    
    print(data)
    print(data.keys())
    
    plt.gcf().canvas.set_window_title(fileName)
    ax = plt.gca()
    ax.set_title("gaussian fitting")
    x = data['gonx'][250:-401]
    y = data['i_pin'][250:-400]
    dy = np.diff(y)
    
    def initialGuess():    
        peak = 0.04
        center = -1.3
        FWHM = fullWidthAtHalfMaximum = 0.1
        k = 2 * sqrt(2 * log(2))
        standard_deviation = FWHM / k
        return [peak, center, standard_deviation]
    fit, estimated_covariance = curve_fit(gauss, x, dy, p0=initialGuess())
    print(fit)
    plt.plot(x, dy)
    ax.set_xlabel('gonx')
    ax.set_ylabel('d(i_pin)')

    plt.plot(x, gauss(x, *fit), 'r-',
             label=f'peak={fit[0]:.2f} μ={fit[1]:.2f} σ={fit[2]:.2f}')
    plt.legend()
    plt.show()


main()

