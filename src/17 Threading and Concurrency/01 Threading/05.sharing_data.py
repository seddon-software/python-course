'''
Sharing Data
============
As discussed previously, code using += is now thread safe.  However, if we look at a more complicated example we can create
some code that is not thread safe.  

In this rather artificial example, we copy a global variable into a local variable, increment the local and finally store the 
result back in the global; the code ends up not thread safe.

Note the use of a call a function (that doesn't do anything) to maximise the chance of being suspended in the critical section of code.
If we remove this call (DELAY=False) then he code is unlikely to go wrong.
'''

import threading

N = 100*1000
NUMBER_OF_THREADS = 10
REPEATS = 20
DELAY = True

# this global counter is not protected by a lock
counter = 0

def delay():
    pass

def increaseCounters(lock):
    global counter
    for _ in range(N):
        n = counter
        if DELAY: delay()
        n += 1
        if DELAY: delay()
        counter = n


def create_and_start_threads(threads, lock):
    for _ in range(NUMBER_OF_THREADS):
        thread = threading.Thread(target=increaseCounters, args=(lock,))
        threads.append(thread)
        thread.start()

def repeat():
    global counter
    counter = 0
    threads = []
    lock = threading.Lock()
    create_and_start_threads(threads, lock)
    for thread in threads:
        thread.join()

    print(f"actual value of counter:  {counter:8}")

print(f"expected value of counter:{N * NUMBER_OF_THREADS:8}")
for _ in range(REPEATS): repeat()

# try without calling delay()
DELAY = False
for _ in range(REPEATS): repeat()