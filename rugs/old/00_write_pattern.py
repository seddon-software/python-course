'''
This program is garbage at present
'''
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

fig = np.load("rugs/figure.npy")
print(fig.shape)
for n in range(10, 20):
    a1 = fig[n]
    a2 = fig[n+32]
    print(n, np.array_equal(a1, a2))
#
# grey          (d) dark brown
# purple        (o) orange
# orange        (p) pink
# lime          (l) pale green
# beige         (b) beige
# white         (w) white
# sage          (g) dark green
# yellow        (y) yellow
# teal          (t) blue
# chestnut      (m) mid brown

