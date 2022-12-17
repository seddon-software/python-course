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
    future.set_result({'index':x, 'fib': await fib(x)})


async def main(n):
    futures = [asyncio.Future() for n in range(n)]
    tasks = [asyncio.create_task(myCoroutine(futures[i], i)) for i in range(n)]
    [await task for task in tasks]
    for future in futures:
        result = future.result()
        print(f"fib({result['index']}) = {result['fib']}")

loop = asyncio.run(main(n=15))
