import numpy as np
from numpy import sin, cos, pi as π
import matplotlib.pyplot as plt
np.set_printoptions(precision=2, linewidth=140)

for row in range(2,11):
    for col in range(2,11):
        print(f"{row*col:3}", end="")
    print()
#image = image.astype(float) / 256
#print(repr(image))
#print(np.array2string(image, separator=','))        