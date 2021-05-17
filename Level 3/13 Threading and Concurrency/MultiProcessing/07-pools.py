############################################################
#
#    using a pool of processes
#
############################################################

from multiprocessing import Pool
import os

''' same as previous example, but this time show process ids'''

def reportProcessIdsOnce():
    try:
        f.called
    except AttributeError:
        f.called = True
        print(f"{os.getppid()} <-- {os.getpid()}")

def f(x):
    reportProcessIdsOnce()  # print pids of processes in pool
    return x**2

with Pool(5) as p:
    print(p.map(f, range(20)))
