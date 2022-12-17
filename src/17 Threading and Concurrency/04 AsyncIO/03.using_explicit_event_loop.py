'''
Explicit Event Loop
===================

The asyncio event loop is created implicitly with
            asyncio.run(main())
            
The alternative is to specify the event loop explicitly as in this example.  Normally this is unnecessary.
'''

import asyncio

async def Fib(n):
    async def fib(n):
        await asyncio.sleep(0.00001)
        return n if n < 2 else await fib(n-1) + await fib(n-2)
    result = await fib(n)
    print(f"fib({n}) = {result}")
    return result

async def main():
    task1 = loop.create_task(Fib(23))
    task2 = loop.create_task(Fib(21))
    task3 = loop.create_task(Fib(15))
    task4 = loop.create_task(Fib(7))
    await asyncio.wait([task1, task2, task3, task4])

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()

