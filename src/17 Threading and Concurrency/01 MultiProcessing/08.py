'''
Executors IO Intensive
=======================
The concurrent.futures module offers facilities for pooling processes, equivalent to using the multiprocessing
pools.  Which you use is a matter of taste.

As we have seen before, pools of processes are generally faster the pools of threads because of the GIL when we are 
considering cpu intensive calculations.  Thread pools work well for IO bound operations. 
'''

from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import ThreadPoolExecutor
import os, time
import requests

# if the work is IO intensive, threads should be slightly faster than processes
def work(n):
    pid = os.getpid()
    requests.get("http://abc.com")
    return n, pid


def compute(executor, name):
    start = time.time()
    futures = [executor.submit(work, n) for n in range(JOBS)]
    results = [futures[n].result() for n in range(JOBS)]
    print(f"\n\n{name} took {time.time() - start:.1f} secs")
    # pids = set(zippedResults[0])
    # totals = zippedResults[1]
    # print(f"pids = {pids}")
    # print(f"{len(totals)} results:")
    # print([f"total = {total:6.2f}" for total in totals])

if __name__ == '__main__': 
    # N = 1000000
    JOBS = 1000 
    with ProcessPoolExecutor(max_workers=50) as executor: compute(executor, "processes")
    with ThreadPoolExecutor(max_workers=50) as executor: compute(executor, "threads")
