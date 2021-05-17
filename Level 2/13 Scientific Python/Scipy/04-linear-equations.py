############################################################
#
#    linear equations
#
############################################################

from numpy import *
from scipy.linalg import solve

# x = 5, y = 3, z = 1

# 5x - 2y + 3z = 22 
# 6x +  y +  z = 34
# 2x - 5y - 2z = -7

a = array( [ [5,-2, 3],
             [6, 1, 1],
             [2,-5,-2] ])
b = array( [22,34,-7] )
result = solve(a, b)
print(result)


1