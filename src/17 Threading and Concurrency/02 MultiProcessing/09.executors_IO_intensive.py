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
    requests.get("https://www.nytimes.com/puzzles/sudoku/easy")
    requests.get("https://www.nytimes.com/puzzles/sudoku/medium")
    requests.get("https://www.nytimes.com/puzzles/sudoku/hard")

def compute(executor, name):
    futures = [executor.submit(work) for job in range(JOBS)]
    results = [futures[job].result() for job in range(JOBS)]

def threadPools():
    with ThreadPoolExecutor(max_workers=50) as executor: compute(executor, "threads")

def processPools():
    with ProcessPoolExecutor(max_workers=50) as executor: compute(executor, "processes")

if __name__ == '__main__': 
    JOBS = 25
    REPEATS = 5

    secs = timeit.timeit(setup="from __main__ import threadPools", stmt="threadPools()", number=REPEATS)
    print(f"threads took {secs:6.2f} secs")

    secs = timeit.timeit(setup="from __main__ import processPools", stmt="processPools()", number=REPEATS)
    print(f"processes took {secs:6.2f} secs")
