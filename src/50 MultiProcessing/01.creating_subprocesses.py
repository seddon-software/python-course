'''
Creating Subprocesses
=====================
The multiprocessing module makes it easy to run code in a subprocess.  As discussed elsewhere, CPU intensive
programs do not scale well ith Python threads because of the Global Interpreter Lock (GIL).  However, by 
running code in subprocesses you will avoid problems with the GIL and gain significant performance boosts.

This is a simple example that runs code in a subprocess.  We print out the process PID to illustrate what
runs where.
'''

import multiprocessing as mp
import os

def fn(N):
    print(f"fn() is executing in process: {os.getpid()}")
    for n in range(N):
        print(n, end=" ")
    print()

if __name__ == '__main__': 
    print(f"Parent process: {os.getpid()}")
    p = mp.Process(target=fn, args=(20,))
    p.start()
    p.join()