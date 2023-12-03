'''
As an alternative you can run multiple tasks with implicit futures.  In this case use use "asyncio.gather"
to obtain results; asyncio.gather automatically waits for all tasks to complete
'''

import asyncio


async def myCoroutine(x):
    async def fib(n):
        await asyncio.sleep(0.01)
        return n if n < 2 else await fib(n-1) + await fib(n-2)
    return {'index':x, 'result': await fib(x)}

async def main(n):
    # note each task yields immediately so that other tasks can run in parallel.  
    tasks = [asyncio.create_task(myCoroutine(i)) for i in range(n)]
    
    # ayncio.gather waits until all results are available before returning
    responses = await asyncio.gather(*tasks)
    for r in responses:
        print(f"fib({r['index']}) = {r['result']}")

asyncio.run(main(n=15))
