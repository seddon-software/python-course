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

image = np.zeros((20,20,3), dtype=int)
print(image.shape)

R = 10
C = 10
for row in range(R):
    ch = "[\n" if row == 0 else ""
    print(ch, end="")
    for col in range(C):
        ch = "    [" if col == 0 else ""
        print(ch, end="")
        for rgb in range(4):
            ch = "[" if rgb == 0 else ""
            print(ch, end="")
            x = (row+5) * (col+5) * (rgb + 1) % 256
            if rgb == 3: x = 200 if row < 6 and col < 6 else 100
            end = "]" if rgb == 3 else ","
            print(f"{x:3}", end=end)
        end = "],\n" if col == C-1 else ","
        print("", end=end)
print("]")

#image = image.astype(float) / 256
#print(repr(image))
#print(np.array2string(image, separator=','))        