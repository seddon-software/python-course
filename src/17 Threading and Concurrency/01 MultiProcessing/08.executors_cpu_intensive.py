'''
Executors CPU Intensive
=======================
The concurrent.futures module offers facilities for pooling processes, equivalent to using the multiprocessing
pools.  Which you use is a matter of taste.

As we have seen before, pools of processes are generally faster the pools of threads because of the GIL when we are 
considering cpu intensive calculations.  Thread pools work well for IO bound operations. 
'''

from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import ThreadPoolExecutor
import os, time

# if the work is CPU intensive, threads should be slower than processes
def work(n, N):
    pid = os.getpid()
    sum_ = 0
    for k in range(N):
        # some complicated calculation
        sum_ += (k/10)**(1/n**2)
    return pid, sum_


def compute(executor, name):
    start = time.time()
    futures = [executor.submit(work, n+1, N) for n in range(JOBS)]
    results = [futures[n].result() for n in range(JOBS)]
    print(f"\n\n{name} took {time.time() - start:.1f} secs")
    zippedResults = list(zip(*results))
    pids = set(zippedResults[0])
    totals = zippedResults[1]
    print(f"pids = {pids}")
    print(f"{len(totals)} results:")
    print([f"total = {total:6.2f}" for total in totals])

if __name__ == '__main__': 
    N = 1000000
    JOBS = 20 
    with ProcessPoolExecutor(max_workers=10) as executor: compute(executor, "processes")
    with ThreadPoolExecutor(max_workers=10) as executor: compute(executor, "threads")
