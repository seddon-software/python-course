############################################################
#
#    miscellaneous
#
############################################################

from numpy import *
from scipy import misc

# factorial
print("factorial(23) =", misc.factorial(23))
print("factorial(23) =", misc.factorial(23, exact=1))
a = array( [ 23,40,17] )
print("factorial(array) =", misc.factorial(a))

# differentiation
print("derivative of x**2 at x=5", end=' ') 
print(misc.derivative(lambda x:x**2, 5))
print("derivative of x**5 at x=5", end=' ')
print(misc.derivative(lambda x:x**5, 5, dx=0.0001))
print(misc.derivative(lambda x:x**5, 5, dx=0.000001))
print(misc.derivative(lambda x:x**5, 5, dx=0.00000001))

# combinations
print("2 from 5 = ", misc.comb(5,2))        
print("13 from 52 = ", misc.comb(52,13))        


1