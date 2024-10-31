import os; os.system("clear")
'''
We can run multiple async tasks, each defined with a future object.  In this example we run a coroutine that calls a recursive
"fib" routine.  Each "fib" populates its own future with its Fibonacci number.
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
    # define a set of futures
    futures = [asyncio.Future() for n in range(n)]

    # create a task corresponding to each future
    tasks = [asyncio.create_task(myCoroutine(futures[i], i)) for i in range(n)]

    # await all the tasks using a comprehension
    [await task for task in tasks]

    # now print the results from each future
    for future in futures:
        result = future.result()
        print(f"fib({result['index']}) = {result['fib']}")

loop = asyncio.run(main(n=15))
