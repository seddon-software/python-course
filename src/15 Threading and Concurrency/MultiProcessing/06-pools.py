############################################################
#
#    using a pool of processes
#
############################################################

from multiprocessing import Pool
import os

def f(x):
    return x**2

# run the map function in parent process
results = list(map(f, range(20)))
print(f"single process: {results}")

# now use the map function provided by the multiprocessing module
# to perform the same operation, but split across a pool of 5 processes
# this function aggregates the results from each child process

with Pool(5) as p:
    results = p.map(f, range(20))
    
print(f"multiple processes: {results}")        
