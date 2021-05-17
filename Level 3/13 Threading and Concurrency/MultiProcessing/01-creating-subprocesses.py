############################################################
#
#    executing code in a subprocess
#
############################################################

import multiprocessing as mp
import os

def fn(N):
    print(f"fn() is executing in {os.getpid()}")
    for n in range(N):
        print(n, end=" ")

if __name__ == '__main__': 
    print(f"Parent process: {os.getpid()}")
    p = mp.Process(target=fn, args=(20,))
    p.start()
    p.join()