import math
import matplotlib.pyplot as plt
import numpy as np
import timeit

X = []
Y = []

for i in range(1,10):
    n = 100 * 2**i
    stmt = f"""
def isprime(num):
    return not [y for y in range(2,num) if num%y==0]

primes = [x for x in range(2,{n}) if isprime(x)]
"""
    Y.append( timeit.timeit(stmt=stmt, number=1) )
    X.append( n )

plt.plot(X, Y)
plt.show()

