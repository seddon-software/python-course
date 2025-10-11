'''
Synchronizing Processes
=======================
When you are running code concurrently in multiple processes, you often need to synchronise code using locks.  Normally locks
only work within a single process, but this example uses special multiprocessor locks:
            import multiprocessing as mp
            lock = mp.Lock()

that work across process boundarries.  In this example the "print()" function's output gets garbled unless you synchronize output 
with:
            synchronize = True
to enable the locking to operate.
'''

import multiprocessing as mp
import time
import random, os

def fn(lock):
    for n in range(10):
        if synchronize: lock.acquire()
        print(f"This is ", end="")
        time.sleep(random.random())
        print(f"process ", end="")
        time.sleep(random.random())
        print(f"{os.getpid()}")
        time.sleep(random.random())
        if synchronize: lock.release()

if __name__ == '__main__': 
    ''' output will be garbled unless synchronize = True '''
    synchronize = True

    processes = []
    lock = mp.Lock()
    for n in range(10):
        p = mp.Process(target=fn, args=(lock,))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
