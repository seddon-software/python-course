import os; os.system("clear")
'''
Here is a simple example that illustrates the concurrent execution of coroutines; even though it is a CPU intensive example.  
We will look at IO examples in due course.
'''

import asyncio
import threading
import os
N = 20

async def square():
    threadId = threading.get_native_id()
    result = f"pid: {os.getpid()}, thread: {threadId}, squares = "
    for n in range(1, N):
        await asyncio.sleep(1)
        result = f"{result} {n**2}"
        print(result)

async def cube():
    threadId = threading.get_native_id()
    result = f"pid: {os.getpid()}, thread: {threadId}, cubes = "
    await asyncio.sleep(1)
    for n in range(1, N):
        await asyncio.sleep(1)
        result = f"{result} {n**3}"
        print(result)

async def quad():
    threadId = threading.get_native_id()
    result = f"pid: {os.getpid()}, thread: {threadId}, quads = "
    for n in range(1, N):
        await asyncio.sleep(1)
        result = f"{result} {n**4}"
        print(result)

async def main():
    # schedule each coroutine
    task1 = asyncio.create_task(square())
    task2 = asyncio.create_task(cube())
    task3 = asyncio.create_task(quad())
    # run them
    await asyncio.wait([task1, task2, task3])

if __name__ == '__main__':
    asyncio.run(main())

