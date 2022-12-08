'''
AsyncIO
=======

The async/await keywords are introduced in Python 3.5 to make grammar of coroutine programming more meaningful.
These coroutines are slightly different from earlier coroutines in that they generate data but do not consume
data.  They are primary aimed at providing concurrency for IO based applications.

Note that all new style coroutine functions must be adorned with the "async" keyword and must be awaited by
their calling coroutine.  To yield control a coroutine has to call:
            asyncio.sleep()

Even sleeping for 0 seconds is sufficient to yield control.

The asyncio module in which these new style coroutines are defined differs from the more traditional threading 
or multiprocess approach to concurrency in that it utilizes an event loop to handle the scheduling of asynchronous
‘tasks’ instead of relying on the kernel to perform the scheduling.

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

Asyncio is intended to work in a single thread and it uses coroutines (i.e. generators) to switch between tasks.  
It utilises an event loop in much the same way as a Graphical User Interface works.  Thus asyncio is an alternative
to using multiple threads and because it is single threaded you don't tend to need locks.
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
