'''
Sharing Data
============

In this example we increment the two global counters using multiple threads.  Only one of the counters is
protected by a lock.  Note how the unprotected counter gets corrupted when you run the code.

Note: You might have to run the code several times to see the data corruption.  Use the script provided:
    run_sharing_data
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
    return counter


def increaseCounters(lock):
    global counter1, counter2
    for i in range(N):
        counter1 = inc(counter1)
        lock.acquire()
        counter2 = inc(counter2)
        lock.release()


def create_and_start_threads():
    lock = threading.Lock()
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


