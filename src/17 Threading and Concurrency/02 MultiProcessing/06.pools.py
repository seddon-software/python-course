'''
Pools
=====
The Pool class allows you to easily create a pool of processes to share the load on a complex computation. 

Notes:
    1) This program does not run well in vscode; run it on the terminal
    2) For lower values of N, the version that doesn't use pools can be faster
'''

from multiprocessing import Pool

import os
import timeit

def SingleProcess():
    results = list(map(f, range(N)))
    #    print(f"single process: {results}")

def PoolOfProcesses():
    # now use the map function provided by the multiprocessing module
    # to perform the same operation, but split across a pool of 5 processes
    # this function aggregates the results from each child process
    with Pool(12) as p:
        results = p.map(f, range(N))    
    #    print(f"multiple processes: {results}")        

def f(x):
    return x**2

if __name__ == '__main__': 
    N = 20000000

    secs = timeit.timeit(setup="from __main__ import PoolOfProcesses", stmt="PoolOfProcesses()", number=1)
    print(f"Pool of Processes takes {secs:6.2f} secs")

    secs = timeit.timeit(setup="from __main__ import SingleProcess", stmt="SingleProcess()", number=1)
    print(f"Single Process    takes {secs:6.2f} secs")
