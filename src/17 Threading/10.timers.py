'''
Timers
======

I should mention the simple Timer:
'''

import time
from threading import Timer
import os; os.system("clear")

def hello():
    print("hello, world")

t = Timer(15.0, hello)
t.start() # after 15 seconds, "hello, world" will be printed
print("waiting for 15 secs ...")
for _ in range(14):
    time.sleep(1)
    print(".", end="")