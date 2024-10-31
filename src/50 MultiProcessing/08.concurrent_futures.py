import os; os.system("clear")
'''
Concurrent Futures
==================

The concurrent.futures module provides a high-level interface for asynchronously executing functions. The ThreadPoolExecutor 
can work synchronously or asynchronously.

In this example we examine both synchronous and asynchronous modes.  In both examples we use "future" objects that handle all 
interactions between threads.  In the asynchronous mode we wait until the "future3" has finished (assumong this future takes the
longest to complete) before querying the results and while we are waiting we print dots to emphasize the asynchrous nature of the 
futures.

In the second example we simply block until all "future" objects obtain their results.
'''

from concurrent.futures import ThreadPoolExecutor
from time import sleep
import sys
 
LIMITA = 2500
LIMITB = 250000
LIMITC = 25000000

def compute1(pool):
    # non blocking, printing dots while calculations in progress

    future1 = pool.submit(sum_of_squares, 1, LIMITA)
    future2 = pool.submit(sum_of_squares, LIMITA+1, LIMITB)
    future3 = pool.submit(sum_of_squares, LIMITB+1, LIMITC)
    while not future3.done():
        sleep(0.25)
        print(".", end="", flush=True)
    
    print()
    print(future1.result() + future2.result() + future3.result())

def compute2(pool):
    # blocking awaiting result
    future1 = pool.submit(sum_of_squares, 1, LIMITA)
    future2 = pool.submit(sum_of_squares, LIMITA+1, LIMITB)
    future3 = pool.submit(sum_of_squares, LIMITB+1, LIMITC)

    # this will block until all results are available
    print(future1.result() + future2.result() + future3.result())

def sum_of_squares(lo, hi):
    total = 0
    for i in range(lo, hi+1):
        total += i**2
    return total
 
if __name__ == '__main__': 
    pool = ThreadPoolExecutor(3)

    print("computing sum of squares using thread pool (non blocking)") 
    compute1(pool)
    print("computing sum of squares using thread pool and blocking until result is available") 
    compute2(pool)
