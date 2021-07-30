import time
from myprogram import *

start_cpu = time.perf_counter()
foo()
foo()
foo()
end_cpu = time.perf_counter()

print(f"time to complete = {end_cpu - start_cpu}")
