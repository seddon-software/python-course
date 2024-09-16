'''
Sharing Data
============
As discussed previously, code using += is now thread safe.  However, if we look at a more complicated example we can create
some code that is not thread safe.  

In this rather artificial example, we copy a global variable into a local variable, increment the local and finally store the 
n between these operations we call a function that doesn't do anything, but this makes the code not thread safe.

If we remove the call to the function (SKIP=True) then the code never goes wrong.
'''

import threading

N = 100*1000
NUMBER_OF_THREADS = 10
REPEATS = 20
SKIP = False

# this global counter is not protected by a lock
counter = 0

def dummy():
    pass

def increaseCounters(lock):
    global counter
    for _ in range(N):
        n = counter
        if not SKIP: dummy()
        n += 1
        if not SKIP: dummy()
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

# try by skipping call to delay()
print("\n*** skipping call to dummy ***\n")
SKIP = True
for _ in range(REPEATS): repeat()
