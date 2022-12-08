'''
run multiple tasks, each with a future
'''

import asyncio
from functools import partial


async def myCoroutine(future, x):
    await asyncio.sleep(1)
    async def fib(n):
        await asyncio.sleep(0.0001)
        return n if n < 2 else await fib(n-1) + await fib(n-2)
    future.set_result(await fib(x))

async def main(n):
    futures = [asyncio.Future() for n in range(n)]
    tasks = [asyncio.create_task(myCoroutine(futures[i], i)) for i in range(n)]
    for i, task in enumerate(tasks):
        await task
        print(f"fib({i}) = {futures[i].result()}")

# Start event loop and run until completed
loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(main(n=15))
finally:
    loop.close()
