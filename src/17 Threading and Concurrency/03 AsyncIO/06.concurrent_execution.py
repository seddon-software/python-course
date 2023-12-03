'''
Here is a simpler example that illustrates the concurrent execution of coroutines.  Note that the 
coroutines run in the same thread.
'''

import asyncio
import threading

async def square():
    threadId = threading.get_native_id()
    result = f"thread: {threadId}, squares = "
    for n in range(1, 10):
        await asyncio.sleep(1)
        result = f"{result} {n**2}"
        print(result)

async def cube():
    threadId = threading.get_native_id()
    result = f"thread: {threadId}, cubes = "
    await asyncio.sleep(1)
    for n in range(1, 10):
        await asyncio.sleep(1)
        result = f"{result} {n**3}"
        print(result)

async def quad():
    threadId = threading.get_native_id()
    result = f"thread: {threadId}, quads = "
    for n in range(1, 10):
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


import warnings
    
if __name__ == '__main__':
    asyncio.run(main())

