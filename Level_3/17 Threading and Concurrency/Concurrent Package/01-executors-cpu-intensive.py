from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import time

# if the work is CPU intensive, threads should be slower than processes

def work(n):
    sum_ = 0
    for n in range(n):
        sum_ += n**0.3
    return sum_


def compute(executor, name):
    r = range(20)
    start = time.time()
    futures = [executor.submit(work, 10*1000*1000) for n in r]
    results = [futures[n].result() for n in r]
    print(f"{name} took {time.time() - start:.1f} secs")

with ThreadPoolExecutor(max_workers=10) as executor: compute(executor, "threads")
with ProcessPoolExecutor(max_workers=10) as executor: compute(executor, "processes")
