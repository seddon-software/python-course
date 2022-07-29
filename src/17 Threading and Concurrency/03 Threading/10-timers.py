'''
Timers
======

I should mention the simple Timer:
'''

from threading import Timer

def hello():
    print("hello, world")

t = Timer(15.0, hello)
t.start() # after 15 seconds, "hello, world" will be printed