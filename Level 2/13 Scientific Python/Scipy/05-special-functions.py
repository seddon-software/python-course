############################################################
#
#    special functions
#
############################################################

from numpy import *
from scipy import special


# Bessel function of real order v at complex z
print(special.jv(6,2+3j))

# Gamma function
print(special.gamma(5))
print(special.gamma(5.1))

# Zeta function
print(special.zeta(10,2))    



1