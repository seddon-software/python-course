'''
Sharing Data
============

Because programmers are prone to forget to release locks, it is safer to use a "try-finally" block to ensure
your lock is always released.  You may prefer the equivalent "with" statement; the "with" statement is 
expanded by the interpreter to the try-finally form (so these forms are equivalent).

Note that often code is modified after the initial design and we might introduce code that could throw an 
exception between obtaining the lock and releasing it.  That's another reason why it's better to use one
of these two forms rather than the direct lock.release() because both forms are exception safe.

Both the functions below use locks to ensure the code is thread safe.
'''

from threading import Thread, Lock
from time import sleep
import threading

counter = 0

def increase(by, lock):
    global counter
    for n in range(10):
        lock.acquire()
        try:
            local_counter = counter
            local_counter += by
            sleep(0.17)
            counter = local_counter
        finally:
            lock.release()

# an alternative form using a "with" context manager
def increase2(by, lock):
    global counter
    for n in range(10):
        with lock:
            local_counter = counter
            local_counter += by
            sleep(0.17)
            counter = local_counter

lock = Lock()

# create threads
t1 = Thread(target=increase2, args=(1, lock))
t2 = Thread(target=increase2, args=(2, lock))

# start the threads
t1.start()
t2.start()

# wait for the threads to complete
t1.join()
t2.join()

print(counter)
