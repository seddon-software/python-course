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
 

def compute1(pool):
    # non blocking, printing dots while calculations in progress

    future1 = pool.submit(sum_of_squares, 1, 100)
    future2 = pool.submit(sum_of_squares, 101, 10000)
    future3 = pool.submit(sum_of_squares, 10001, 100 * 1000 * 1000)
    while not future3.done():
        sleep(0.25)
        print(".", end=" ", flush=True)
    
    print()
    print(future1.result() + future2.result() + future3.result())

def compute2(pool):
    # blocking awaiting result
    future1 = pool.submit(sum_of_squares, 1, 100)
    future2 = pool.submit(sum_of_squares, 101, 10000)
    future3 = pool.submit(sum_of_squares, 10001, 100 * 1000 * 1000)
    # this will block until all results are available
    print(future1.result() + future2.result() + future3.result())

def sum_of_squares(lo, hi):
    total = 0
    for i in range(lo, hi+1):
        total += i**2
    return total
 
if __name__ == '__main__': 
    pool = ThreadPoolExecutor(3)

    print("computing sum of squares using thread pool") 
    compute1(pool)
    print("computing sum of squares using thread pool and blocking until result is available") 
    compute2(pool)
