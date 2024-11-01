'''
Asyncio is designed to solve I/O network performance, not CPU bound operations (which is where multiprocessing 
should be used).  Asyncio is designed around the concept of ‘cooperative multitasking’, so you have to yield 
control to other tasks to allow them to run.

Even though asyncio is intended to work with IO intensive application, it does work with CPU intensive 
applications.  In this example we compute Fibonacci numbers by recursion and the application is clearly CPU
intensive.  Nevertheless, we can run several asyncio tasks concurrently with this library.  All the tasks run 
in the same thread, but because the library is based upon generators (i.e. coroutines) we can switch between
the tasks without the need for multi-threading or multi-tasking.

Notice the calculations will be completed with the simpler calculations finishing first (because all the 
calculations are performed in parallel irrespective of the starting order.

Asyncio is intended to work in a single thread; it utilises an event loop in much the same way as a Graphical User Interface 
works.  Thus asyncio is an alternative to using multiple threads.
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
    task1 = asyncio.create_task(Fib(23))
    task2 = asyncio.create_task(Fib(21))
    task3 = asyncio.create_task(Fib(15))
    task4 = asyncio.create_task(Fib(7))
    await asyncio.wait([task1, task2, task3, task4])

if __name__ == '__main__':
    asyncio.run(main())

