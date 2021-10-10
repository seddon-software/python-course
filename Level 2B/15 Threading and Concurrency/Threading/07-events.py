############################################################
#
#    events
#
############################################################

from threading import Thread
from threading import Event
import random
import time
import sys


class MyClass:
    def __call__(self, name):
        global event
        print((name + " waiting for event"));
        event.wait()
        print(("\t" + name + " proceeding after event"));


event = Event()

m1 = MyClass()
m2 = MyClass()
m3 = MyClass()

t1 = Thread(target = m1, args = ("1",))
t2 = Thread(target = m2, args = ("2",))
t3 = Thread(target = m3, args = ("3",))

t1.start()
t2.start()
t3.start()

print("... main waiting for 15 seconds")
time.sleep(15)
print("... main clearing event flag")
event.set()

t1.join()
t2.join()
t3.join()

print("\nEnd of main")


1
