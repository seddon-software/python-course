import os, time, numpy as np

import cothread
from cothread.catools import *


print(caget("chris:amplitude"))

for n in np.arange(1.0, 0.2, -0.01):
    caput("chris:amplitude", n)
    time.sleep(0.1)

