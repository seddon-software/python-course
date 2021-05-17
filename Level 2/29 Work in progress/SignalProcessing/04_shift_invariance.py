import numpy as np
import matplotlib.pyplot as plt

def h(k):
    if k == 0:
        return 1
    elif k < 0 or k > 10:
        return 0
    else:
        return (np.exp(1/k) - 1) / np.exp(1)

def x(k):
    if k < 0:
        return 0
    elif k > 10:
        return 0
    else:
        return 1
        
        
def y(n):
    return sum([x(k)*h(n-k) for k in range(-40, 40)])

h = np.vectorize(h, otypes=[np.float])
y = np.vectorize(y, otypes=[np.float])
n = range(-10, 20)

X = range(-15, 20)
Y = y(X)
plt.bar(X, Y) 
plt.grid(True)
plt.show()   
