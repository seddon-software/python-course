'''
11 Introduction to Functional: some parts not covered

spreadsheets
14 Testing
15 Threading and Concurrency
'''

import numpy as np
from numpy import sin, cos, pi as π
import matplotlib.pyplot as plt


X = np.arange(1, 5, 0.001)
Y = sin(2*π*X)/X**2    
    
plt.plot(X, Y)
plt.grid()
plt.show()

