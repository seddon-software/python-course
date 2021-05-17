import numpy as np
import pylab as plt
from scipy.optimize import curve_fit

# define a square function with 3 unknowns: a, b and c
def square(n, a, b, c): 
    return a * n**2 + b * n + c


# define some 'experimental' results
X = np.array([1.00,  2.00,  3.00,  4.00,  5.00,  6.00])
Y = np.array([2.22, 10.08, 17.82, 34.06, 54.86, 70.06])
plt.plot(X, Y, 'ro')

# perform a non-linear least squares fit
fit, estimatedCovariance = curve_fit(square, X, Y)
results = f"a = {fit[0]:5.2f}\nb = {fit[1]:5.2f}\nc = {fit[2]:5.2f}\n"
plt.xlabel("$x$", fontsize=16)
plt.ylabel("$x^2$", fontsize=16, labelpad=20, rotation=0)
plt.title("Least Squares Fit", fontsize=16)

# plot fitted curve
X = np.arange(0, 6, 0.01)
Y = [square(x, *fit) for x in X]
plt.plot(X, Y, color='blue', lw=2, label=results)
plt.legend(loc = 2)
plt.tight_layout()  # make sure everything fits in window

plt.show()

