'''
coroutine tasks (async_worker) run in parallel and scale well.  Here we run N (=1000) coroutines at the same time.  Compare
that with running 1000 synchronous  tasks (sync_worker).  The sync_workers take N * random.random() seconds to complete.
That works out as ~1000 * 0.5 = ~50 secs.  Compare that with the very short time the coroutines take to complete. 
'''

import asyncio
import time
import random
import time

N = 1000

async def async_worker(i: int):
    await asyncio.sleep(random.random() * .1)
    return i

def sync_worker(i: int):
    time.sleep(random.random() * .1)
    return i

async def async_code():
    start = time.perf_counter()
    tasks = [asyncio.create_task(async_worker(i)) for i in range(N)]
    results = await asyncio.gather(*tasks)
    end = time.perf_counter()

    print(f"Completed {len(results)} tasks")
    print(f"Time taken: {end - start:.4f} seconds")

def sync_code():
    start = time.perf_counter()
    results = [sync_worker(i) for i in range(N)]
    end = time.perf_counter()
    print(f"Completed {len(results)}")
    print(f"Time taken: {end - start:.4f} seconds")

if __name__ == "__main__":
    asyncio.run(async_code())
    sync_code()

