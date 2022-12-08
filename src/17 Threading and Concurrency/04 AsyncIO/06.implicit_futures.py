'''
run multiple tasks with implicit futures; i.e. use asyncio.gather instead
'''

import asyncio


async def myCoroutine(x):
    async def fib(n):
        await asyncio.sleep(0)
        return n if n < 2 else await fib(n-1) + await fib(n-2)
    return {'index':x, 'result': await fib(x)}

async def main(n):
    tasks = [asyncio.create_task(myCoroutine(i)) for i in range(n)]
    responses = await asyncio.gather(*tasks)
    for r in responses:
        print(f"fib({r['index']}) = {r['result']}")

# Start event loop and run until completed
loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(main(n=15))
finally:
    loop.close()
