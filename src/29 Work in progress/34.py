import numpy as np
from numpy import sin, cos, pi as π
import matplotlib.pyplot as plt
np.set_printoptions(precision=2, linewidth=140)

def gen():
    n = 0
    while True:
        yield n
        n += 1
        n = n % 256
        

g = gen()

image = np.zeros((20,20), dtype=int)
print(image.shape)

for row in range(20):
    for col in range(20):
        x = next(g)
        image[row,col] = (row+5) * (col+5) % 256

image = image.astype(float) / 256
print(repr(image))
        