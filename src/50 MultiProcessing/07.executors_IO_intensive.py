'''
Executors IO Intensive
=======================
When an application is IO intensive, the GIL is much less important and pools of threads work as well as pools
of processes. 
'''

from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import timeit
import requests


def work():
    requests.get("https://docs.python.org/3/")
    requests.get("https://numpy.org/doc/")
    requests.get("https://matplotlib.org/stable/index.html")

def compute(executor):
    futures = [executor.submit(work) for job in range(JOBS)]

def threadPools():
    with ThreadPoolExecutor(max_workers=6) as executor: compute(executor)

def processPools():
    with ProcessPoolExecutor(max_workers=6) as executor: compute(executor)

if __name__ == '__main__': 
    print("perform I/O intensive work")
    JOBS = 25
    REPEATS = 10

    secs = timeit.timeit(setup="from __main__ import threadPools", stmt="threadPools()", number=REPEATS)
    print(f"threads took {secs:6.2f} secs")

    secs = timeit.timeit(setup="from __main__ import processPools", stmt="processPools()", number=REPEATS)
    print(f"processes took {secs:6.2f} secs")
