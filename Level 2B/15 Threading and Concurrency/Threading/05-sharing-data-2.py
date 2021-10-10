############################################################
#
#    sharing data
#
############################################################

from threading import Thread
from threading import Lock
import random
import time
import sys


# locks should be released in a finally block
# just in case ...

class MyClass:
    def __call__(self, name):
        global lock, count1, count2
        for i in range(0, 2*1000*1000):
            count1 += 1
            lock.acquire()
            try:
                count2 += 1
            finally:
                lock.release()  # release even if exception

    
lock = Lock()
count1 = 0
count2 = 0

m1 = MyClass()
m2 = MyClass()
m3 = MyClass()

t1 = Thread(target = m1, args = ("1",))
t2 = Thread(target = m2, args = ("2",))
t3 = Thread(target = m3, args = ("3",))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("count1: " + str(count1))
print("count2: " + str(count2))

print("\nEnd of main")
