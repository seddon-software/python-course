'''
The time module provides various time-related functions.  

The perf_counter() function returns the elapsed time in seconds, accurate to the highest available resolution
available.  To obtain timing, we take the difference between two readings.
'''

import time
from myprogram import *

start_cpu = time.perf_counter()
foo()
foo()
foo()
end_cpu = time.perf_counter()

print(f"time to complete = {end_cpu - start_cpu}")
