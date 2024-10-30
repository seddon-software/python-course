import os; os.system("clear")
'''
Executors CPU Intensive
=======================
The concurrent.futures module offers facilities for pooling processes, theoretically equivalent to using the multiprocessing
pools.  Which you use is a matter of taste (or speed!).

As we have seen before, pools of processes should be faster the pools of threads because of the GIL when we are 
performing cpu intensive calculations.  Thread pools work well for IO bound operations. 

Note the executor sometimes spawns fewer processes than tasks.'''

from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import ThreadPoolExecutor
import os, time
import timeit

# if the work is CPU intensive, threads should be slower than processes
def work(n, N):
    pid = os.getpid()
    sum_ = 0
    for k in range(N):
        # some complicated calculation
        sum_ += (k/10)**(1/n**2)
    return pid, sum_


def compute(executor, details, name):
    # executor returns a list of results, one for each process/thread
    futures = [executor.submit(work, n+1, N) for n in range(JOBS)]  # n+1 so that each task is slightly different
    results = [futures[n].result() for n in range(JOBS)]

    if details:
        print(f"\n\n{name}")

        # zip all the results together (tuple of pids in [0], tuple of sums in [1])
        zippedResults = list(zip(*results))
    
        # remove duplicate pids using a set and then print them
        pids = set(zippedResults[0])
        print(f"pids = {pids}")

        # print all the results
        totals = [float(f"{result:6.2f}") for result in zippedResults[1]]
        print(f"results = {totals}\n\n")

def processPools(details):
    with ProcessPoolExecutor(max_workers=6) as executor: compute(executor, details, "PROCESSES")

def threadPools(details):
    with ThreadPoolExecutor(max_workers=6) as executor: compute(executor, details, "THREADS")

if __name__ == '__main__': 
    print("perform CPU intensive work")

    N = 100000
    JOBS = 20 
    REPEATS = 10

    processPools(True)
    threadPools(True)

    secs = timeit.timeit(setup="from __main__ import processPools", stmt="processPools(False)", number=REPEATS)
    print(f"processes took {secs:6.2f} secs")

    secs = timeit.timeit(setup="from __main__ import threadPools", stmt="threadPools(False)", number=REPEATS)
    print(f"threads took   {secs:6.2f} secs")
