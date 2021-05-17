from concurrent.futures import ThreadPoolExecutor
from time import sleep
import sys
 

def compute1(pool):
    future1 = pool.submit(sum_of_squares, 1, 100)
    future2 = pool.submit(sum_of_squares, 101, 10000)
    future3 = pool.submit(sum_of_squares, 10001, 10 * 1000 * 1000)
    while not future3.done():
        sleep(0.25)
        print(".", end=" ", flush=True)
    
    print()
    print(future1.result() + future2.result() + future3.result())

def compute2(pool):
    future1 = pool.submit(sum_of_squares, 1, 100)
    future2 = pool.submit(sum_of_squares, 101, 10000)
    future3 = pool.submit(sum_of_squares, 10001, 10 * 1000 * 1000)
    # this will block until all results are available
    print(future1.result() + future2.result() + future3.result())

def sum_of_squares(lo, hi):
    total = 0
    for i in range(lo, hi+1):
        total += i**2
    return total
 
pool = ThreadPoolExecutor(3)
 
compute1(pool)
compute2(pool)
