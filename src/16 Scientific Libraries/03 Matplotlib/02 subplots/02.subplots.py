'''
Subplots
========

This is a similar example, but explores creating different sizes of grid for axes.  The results are spread across
3 figures.
'''

import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

def subplot2x1():
    # 2 rows and 1 col
    fig, (ax1, ax2) = plt.subplots(2, 1)
    ax1.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
    ax2.plot(t2, np.cos(2*np.pi*t2), 'r--')

def subplot2x3():
    # 2 rows and 3 cols
    fig, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(2, 3)
    ax1.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
    ax2.plot(t2, np.cos(2*np.pi*t2), 'r--')
    ax3.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
    ax4.plot(t2, np.cos(2*np.pi*t2), 'r--')
    ax5.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
    ax6.plot(t2, np.cos(2*np.pi*t2), 'r--')

def subplot5x4():
    rows = 5
    cols = 4
    fig, ax = plt.subplots(rows, cols)
    for row in range(rows):
        for col in range(cols):
            style = 'r--'
            ax[row, col].plot(t2, np.cos(2*np.pi*t2), style)

subplot2x1()
plt.tight_layout()
subplot2x3()
plt.tight_layout()
subplot5x4()
plt.tight_layout()
plt.show()

