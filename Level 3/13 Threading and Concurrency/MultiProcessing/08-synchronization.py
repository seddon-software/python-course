############################################################
#
#    synchronizing processes
#
############################################################

import multiprocessing as mp
import time, os

''' output will be garbled unless synchronize = True '''
synchronize = True

def fn(lock):
    for n in range(50):
        if synchronize: lock.acquire()
        print(f"This is ", end="")
        print(f"process ", end="")
        print(f"{os.getpid()}")
        if synchronize: lock.release()
        time.sleep(0.005)

if __name__ == '__main__': 
    processes = []
    lock = mp.Lock()
    for n in range(10):
        p = mp.Process(target=fn, args=(lock,))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
