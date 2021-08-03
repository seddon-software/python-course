import numpy as np
np.set_printoptions(precision=3)

x, y = np.mgrid[0:5, 0:5] # similar to meshgrid in MATLAB
print("x = \n", x)
print("y = \n", y)


m = np.diag([2,3,4])
print("m = \n", m)
m = np.diag([2,3,4], k = 2)
print("m = \n", m)
m = np.random.rand(5,5)
print("m = \n", m)
