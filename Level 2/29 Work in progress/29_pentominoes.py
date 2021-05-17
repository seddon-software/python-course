'''
Use a Monte Carlo simulation to prove that a knight can reach
every square on a chess board.

1. Create an 8x8 Numpy array of zeros
2. Write a generator that computes the next move 
3. Fill in numpy array with a 1 corresponding to a move
4. Print array after N iterations
5. What value of N consistently leads to a complete walk of the board?

'''

import numpy as np
import random


f = np.array([[0,1,1],
              [1,1,0],
              [0,1,0]])

def rotate90(x) : return x.T

print(f)
f2 = rotate90(f)
print(f2)
