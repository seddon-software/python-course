import matplotlib.pyplot as plt
import time
import numpy as np

def factorial(n):
    f = 1
    for x in range(2,n+1):
        f = f*x
    return f

def getTime(n):
    t0 = time.time()
    factorial(n)
    t1 = time.time()
    return t1 - t0

getTime = np.vectorize(getTime, otypes=[np.float])

N = 1000*1000       # takes 6 min 20 secs
X = np.arange(N, N+1)
Y = getTime(X)
print(Y)

plt.plot(X,Y)
plt.show()
