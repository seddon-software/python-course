############################################################
#
#    solving non linear equations
#
############################################################

from scipy import *
from scipy.optimize import fsolve
from matplotlib import pylab
from pylab import *
"""
Use fsolve to find intersections of exp(x)-1 with cos(x)
Note that need different guesses to find different intersections
"""
def f(x):
    return (exp(x)-1)-cos(x)

# use fsolve to solve exp(x)-1  -  cos(x) = 0
guess =   2.0; print(fsolve(f,guess))
guess =  -1.0; print(fsolve(f,guess))
guess =  -5.0; print(fsolve(f,guess))
guess =   0.0; print(fsolve(f,guess))
guess = -10.0; print(fsolve(f,guess))

# plot the graph to see if we are correct
x = linspace(-15,1,401)
plot(x,exp(x)-1, x,cos(x))
grid(b=1)
show()

1