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


def generateNewPosition():
    possibleMove = np.array([(-1,2),(+1,2),(-1,-2),(-1,2),(-2,-1),(-2,1),(2,-1),(2,1)])
    position = np.array((2, 3))
    yield position
    while(True):
        n = random.getrandbits(3)
        nextTry = possibleMove[n] + position
        if np.amax(nextTry) < 8 and np.amin(nextTry) >= 0:
            position = nextTry
        yield position
        

board = np.zeros((8,8), dtype=int)

g = generateNewPosition()

for move in range(20000):
    move = next(g)
    board[move[0],move[1]] = 1
    
print(board)

    
    
    
    