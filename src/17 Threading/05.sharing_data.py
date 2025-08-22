'''
Sharing Data
============
As discussed previously, code using += is now thread safe.  However, if we look at a more complicated example we 
can create some code that is not thread safe.  

In this rather artificial example, we copy a global variable into a local variable, increment the local using +=
and finally store back in the global.  In between these operations we call a function that doesn't do anything, 
but this stops the code being thread safe.

If we remove the call to the function (SKIP=True) then the code never goes wrong.

Note: This code behaves differently in older versions of Python.  In Python <=3.10 the code is never "thread safe".  
In Python 3.11+ the code is only thread safe if SKIP=True
'''

import threading

# print("*** This example uses Python 3.11+")
N = 250*1000
NUMBER_OF_THREADS = 2

# this global counter IS NOT protected by a lock
counter1 = 0
# this global counter IS protected by a lock
counter2 = 0

def inc(counter):
    counter += 1
    dummy()
    return counter

def dummy(): pass
def progress(i):
    if i % (N/100) == 0: 
        v = (100*i)//N
        print(f"{v}%")

def increaseCounters(lock):
    global counter1, counter2
    for i in range(N):
        counter1 = inc(counter1)
        lock.acquire()
        counter2 = inc(counter2)
        lock.release()
        # progress(i)

lock = threading.Lock()

def create_and_start_threads():
    listOfThreads = []
    for _ in range(NUMBER_OF_THREADS):
        thread = threading.Thread(target=increaseCounters, args=(lock,))
        thread.start()
        listOfThreads.append(thread)
    return listOfThreads


threads = create_and_start_threads()
[thread.join() for thread in threads]
    
print(f"expected value of counters:{N * NUMBER_OF_THREADS:8}")
print(f"actual value of counter1:  {counter1}")
print(f"actual value of counter2:  {counter2}")


