############################################################
#
#    semaphores
#
############################################################

from threading import Thread
from threading import BoundedSemaphore
import random
import time
import sys


class MyClass:
    def __call__(self, name):
        global semaphore
        semaphore.acquire()
        print((name + " claimed semaphore"));
        time.sleep(5)
        print(("\t" + name + " released semaphore"));
        semaphore.release()



semaphore = BoundedSemaphore(3)

m1 = MyClass()
m2 = MyClass()
m3 = MyClass()
m4 = MyClass()
m5 = MyClass()
m6 = MyClass()
m7 = MyClass()

t1 = Thread(target = m1, args = ("1",))
t2 = Thread(target = m2, args = ("2",))
t3 = Thread(target = m3, args = ("3",))
t4 = Thread(target = m4, args = ("4",))
t5 = Thread(target = m5, args = ("5",))
t6 = Thread(target = m6, args = ("6",))
t7 = Thread(target = m7, args = ("7",))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()

print("\nEnd of main")

1
