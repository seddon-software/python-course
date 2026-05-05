'''
Sometimes you want to reuse some synchronous code in an asynchronous application without rewriting the code.
You can run such code either in separate threads or in separate process.

The code below shows the normal approach.
'''

import asyncio
import time
from concurrent.futures import ProcessPoolExecutor

def Fib1(n):
    def fib(n):
        return n if n < 2 else fib(n-1) + fib(n-2)
    result = fib(n)
    print(f"Thread fib({n}) = {result}")
    return result

def Fib2(n):
    def fib(n):
        return n if n < 2 else fib(n-1) + fib(n-2)
    result = fib(n)
    print(f"Process fib({n}) = {result}")
    return result

async def threads():
    # Run in Threads (implicit thread pool)
    task1 = asyncio.create_task(asyncio.to_thread(Fib1, 37))
    task2 = asyncio.create_task(asyncio.to_thread(Fib1, 22))
    task3 = asyncio.create_task(asyncio.to_thread(Fib1, 39))
    task4 = asyncio.create_task(asyncio.to_thread(Fib1, 24))

    result1 = await task1
    result2 = await task2
    result3 = await task3
    result4 = await task4
    return [result1, result2, result3, result4]

async def processes():
    # run in Process Pool
    loop = asyncio.get_running_loop()

    with ProcessPoolExecutor() as executor:
        task1 = loop.run_in_executor(executor, Fib2, 37)
        task2 = loop.run_in_executor(executor, Fib2, 22)
        task3 = loop.run_in_executor(executor, Fib2, 39)
        task4 = loop.run_in_executor(executor, Fib2, 24)

        result1 = await task1
        result2 = await task2
        result3 = await task3
        result4 = await task4
    return f"{[result1, result2, result3, result4]}"


if __name__ == "__main__":
    def run_in_threads():
        start = time.perf_counter()
        results = asyncio.run(threads())
        finish = time.perf_counter()
        print(f"{results}\nFinished in {finish - start:.2f} seconds")
    def run_in_processes():
        start = time.perf_counter()
        results = asyncio.run(processes())
        finish = time.perf_counter()
        print(f"{results}\nFinished in {finish - start:.2f} seconds")
        
    run_in_threads()
    run_in_processes()
