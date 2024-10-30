import os; os.system("clear")
'''
Pools
=====
The Pool/ThreadPool class allows you to easily create a pool of processes/threads to share the load on a complex computation. 

Not: The map function has 2 parameters:
    parameter-1:    the transform to apply
    parameter-2:    the iterable to transform

Thus all items in the iterable get transformed.
'''

POOL_SIZE = 12
NUMBER = 1

from multiprocessing import Pool
from multiprocessing.pool import ThreadPool

import os, timeit

def SingleProcess():
    # results = map(f, range(N))
    results = map(work, range(2,N))
    return sum(results)

def PoolOfThreads():
    # now use the map function provided by the multiprocessing module
    # to perform the same operation, but split across a pool of POOL_SIZE threads
    # this function aggregates the results from each child process
    with ThreadPool(POOL_SIZE) as pool:
        results = pool.map(work, range(2,N))
    return sum(results)

def PoolOfProcesses():
    # now use the map function provided by the multiprocessing module
    # to perform the same operation, but split across a pool of POOL_SIZE processes
    # this function aggregates the results from each child process
    with Pool(POOL_SIZE) as pool:
        results = pool.map(work, range(2,N))
    return sum(results)

def work(n):
    # some complicated calculation
    return (n/10)**(1/n**2) + (n/7)**(3/n**3)

N = 10000000

if __name__ == '__main__': 
    print("Computing cpu intensive calculations")
    print(f"{'Processes:':20}", end="", flush=True)
    print(f"{PoolOfProcesses():10.2f}")
    print(f"{'Threads:':20}", end="", flush=True)
    print(f"{PoolOfThreads():10.2f}")
    print(f"{'Single Process:':20}", end="", flush=True)
    print(f"{SingleProcess():10.2f}")

    secs = timeit.timeit(setup="from __main__ import PoolOfProcesses", stmt="PoolOfProcesses()", number=NUMBER)
    print(f"Pool of Processes takes {secs:6.2f} secs")

    secs = timeit.timeit(setup="from __main__ import PoolOfThreads", stmt="PoolOfThreads()", number=NUMBER)
    print(f"Pool of Threads takes   {secs:6.2f} secs")

    secs = timeit.timeit(setup="from __main__ import SingleProcess", stmt="SingleProcess()", number=NUMBER)
    print(f"Single Process takes    {secs:6.2f} secs")
