'''
Sharing Data
============
As discussed previously, code using += is not thread safe.  As an illustration of this we define a counter and
then increment it in 2 separate threads.  When we set:
            useLocks = False

we get random behaviour (because the code is not thread safe).  Correct behaviour is observed if we set:
            useLocks = True

Note the use of the "sleep" call to maximise the chance of being suspended in the critical section of 
code.
'''

from threading import Thread, Lock
from time import sleep
import threading

counter = 0
useLocks = False

def increase(by, lock):
    global counter
    for n in range(10):
        if useLocks: lock.acquire()

        local_counter = counter
        local_counter += by
        sleep(0.17)
        counter = local_counter

        if useLocks: lock.release()

lock = Lock()

# create threads
t1 = Thread(target=increase, args=(1, lock))
t2 = Thread(target=increase, args=(2, lock))

# start the threads
t1.start()
t2.start()


# wait for the threads to complete
t1.join()
t2.join()

print(counter)
