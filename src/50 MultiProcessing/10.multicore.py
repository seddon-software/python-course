'''
Using Multiple Cores
====================
Normally Python executes on a single core; the Pool module allows you to spread computation across multiple cores.  This program runs indefinitely and intentionally uses 
multiple cores and a lot of CPU.

Notes: 
    use htop to monitor CPUs utilisation.
'''

from multiprocessing import Pool, cpu_count

def some_calculation(x):
    while True:
        x * x

import time
time.sleep(5)
if __name__ == '__main__': 
    print(f"There are {cpu_count()} CPUs on this machine")
    p = Pool(processes=2*cpu_count())
    p.map(some_calculation, range(cpu_count()))

