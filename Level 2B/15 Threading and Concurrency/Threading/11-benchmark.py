import time, os
from threading import Thread
from multiprocessing import Process, Pool
import numpy as np
from itertools import chain

''' Calculate the sum of i**0.3 where i ranges from 0 to M
    Use multiple threads or processes to perform the calculation
    Split the calculation into ranges using the intervals function below
'''

M = 50*1000*1000

def calculate(lo, hi):
    '''the calculation to perform'''
    sum = 0
    for i in range (lo, hi):
        sum += float(i)**0.3
    return sum   

def intervals(duration, parts):
    '''splits an interval into several(part) ranges'''
    part_duration = int(duration / parts)
    return [(int(i * part_duration), int((i + 1) * part_duration)) for i in range(parts)]

# calculate the sum using multiple threads
def jobUsingThreads(threadCount):
    threadList = []
    it = intervals(M, threadCount)
    
    for i in range(threadCount):
        t = Thread(target = calculate, args = it[i])
        t.start()
        threadList.append(t)
        
    for t in threadList:
        t.join()

# calculate the sum using multiple threads
def jobUsingProcesses(processCount):
    p = Pool(processes=processCount)
    it = intervals(M, processCount)
    result = p.starmap(calculate, it)

# run job with varying number of processes
for N in chain(range(1, 11), range(20, 101, 20)):
    start = time.perf_counter()
    jobUsingProcesses(N)
    finish = time.perf_counter()
    print(f"{N:2} processes:{finish-start:6.2f}")

# run job with varying number of processes
for N in chain(range(1, 11), range(20, 101, 20)):
    start = time.perf_counter()
    jobUsingThreads(N)
    finish = time.perf_counter()
    print(f"{N:2} threads:{finish-start:6.2f}")
