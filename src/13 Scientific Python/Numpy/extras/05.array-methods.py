############################################################
#
#    array methods
#
############################################################

import numpy as np

a = np.array( np.random.random(10) * 100, dtype="int" )
print(a)
print(type(a))

print("sum =", a.sum())
print("product =", a.prod())
print("max =", a.max())
print("min =", a.min())
print("mean =", a.mean())
print("standard deviation =", a.std())
print("variance =", a.var())
print("cumlative sum =", a.cumsum())
# perform operations along specified axis
a = np.arange(12).reshape(3,4)
print(a)
print(a.sum(axis=0))
print(a.sum(axis=1))

1
