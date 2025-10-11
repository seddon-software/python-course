'''
Semaphores
==========
Semaphores (aka Bounded Semaphores) are like a set of multiple locks.  

A bounded semaphore is created with an initial count:
            semaphore = BoundedSemaphore(3)

Threads can acquire the semaphore by decrementing the count:
            semaphore.acquire()

However the count can never go negative.  So after 3 threads have acquired the semaphore the next thread will be 
blocked until another thread releases the semaphore and increments the count by one:
            semaphore.release()

This continues until all the threads have acquired and released the semaphore.  Thus this bounded semaphore 
behaves as a set of 3 locks.

Note the locking in printMessage; the output gets garbled if you don't use the lock.
'''

from threading import Thread, BoundedSemaphore
import multiprocessing as mp
import random
import time
import sys

def printMessage(message):
    global lock
    lock.acquire()
    print(message)
    lock.release()

class MyClass:
    def __call__(self, name):
        global semaphore

        semaphore.acquire()
        printMessage(f"{name} claimed semaphore")
        time.sleep(5)
        printMessage(f"\t{name} released semaphore")
        semaphore.release()


lock = mp.Lock()
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
