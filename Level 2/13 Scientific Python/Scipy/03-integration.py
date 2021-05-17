############################################################
#
#    integration
#
############################################################

from scipy import * 
from scipy.integrate import quad
"""
integration using quadrature
"""
def f(x):
    return exp(-x)

# integrate exp(-x) between 0 and 5
result = quad(f, 0, 5)
print("result", result[0])
print("error estimate", result[1])
    
# now use lambda functions
result = quad(lambda x: exp(-x),0,5)
print("calculated result:", result)
print("analytical result:", 1 - exp(-5))

# more tests
print(quad(lambda x: x, 0, 10))
print(quad(lambda x: x**2, 0, 1))
print(quad(lambda x: -x**-2/2.0, 0, 1)) # divergent
print(quad(lambda x: x**-2, 1, inf))


1