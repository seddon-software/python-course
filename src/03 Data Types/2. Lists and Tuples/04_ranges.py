############################################################
#
#    range
#
############################################################

import numpy as np

l = [0, 1, 2, 3, 4, 5, 6]
l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

z = range(2000)
print(type(z))
print(z)
print(list(z))

x = list(range(10, 15, 2))
y = list(range(20,1,-3))
print(x)
print(y)

print(np.arange(1, 2, 0.1))

