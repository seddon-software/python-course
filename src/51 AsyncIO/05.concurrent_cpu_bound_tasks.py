'''
Here is a simple example that illustrates the concurrent execution of coroutines; even though it is a CPU 
intensive example.  This shows the asyncio code to replicate our first example in this section.

We will look at IO examples in due course.
'''

import asyncio

async def power(n):
    x = 1
    while(x <= 10):
        print(f"{x}**{n} = {x**n}")
        x = x + 1
        await asyncio.sleep(1)

async def main():
    # schedule each coroutine
    task1 = asyncio.create_task(power(2))
    task2 = asyncio.create_task(power(3))
    task3 = asyncio.create_task(power(4))
    # await them
    await asyncio.wait([task1, task2, task3])

if __name__ == '__main__':
    asyncio.run(main())

