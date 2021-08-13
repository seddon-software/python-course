import os, time, numpy as np

import cothread
from cothread.catools import *


print(caget("chris:amplitude"))

for n in np.arange(1.0, 0.1, -0.01):
    caput("chris:amplitude", n)
    print(f'{caget("chris:amplitude"):0.2f}')
    time.sleep(0.25)

for n in np.arange(0.1, 1.0, 0.01):
    caput("chris:amplitude", n)
    print(f'{caget("chris:amplitude"):0.2f}')
    time.sleep(0.25)

pvs = ["chris:function",
"chris:amplitude",
"chris:offset",
"chris:counter",
"chris:freqCalc",
"chris:function",
"chris:freqMenu"]

for pv in pvs:
    print(f"{pv}:{caget(pv)}")
