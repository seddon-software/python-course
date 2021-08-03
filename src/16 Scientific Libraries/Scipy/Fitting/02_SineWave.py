import scipy.optimize
import matplotlib.pyplot as plt
import numpy as np

def func(x, a, b):
   return a * np.sin(b * x)


def set_title(title):
    figure = plt.gcf()
    figure.canvas.set_window_title(title)

def experimentalData():
    numberOfPoints = 5000
    X = np.linspace(-5, 5, num=numberOfPoints)
    Y = 2.9 * np.sin(1.5 * X) + np.random.normal(size=numberOfPoints)
    return X, Y

def fit(X, Y):
    # If we know that the data lies on a sine wave, but not the amplitudes or the period, we can find those by least squares curve fitting. First we have to define the test function to fit, here a sine with unknown amplitude and period:
    initialGuess = [1, 1]
    [best_a, best_b], params_covariance = scipy.optimize.curve_fit(func, X, Y, p0=initialGuess)
    print(f"fitted values of a, b: {best_a:6.3f}, {best_b:6.3f}")
    return func(X, best_a, best_b)
    
X, Y1 = experimentalData()
Y2 = fit(X, Y1)
ax = plt.subplot() 
ax.plot(X, Y1, 'b.', X, Y2, 'r.')

plt.show()

