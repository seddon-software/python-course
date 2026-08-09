'''
When you await a coroutine object it will get scheduled immediately and eventually run to completion.
If you do this with several coroutine objects you will find they do not run in parallel.

However, if you wrap a coroutine object inside a task it gets scheduled and put into a pending state.  
If you do this with several coroutine objects they will all be scheduled in a pending state.
Now when any task is awaited the coroutine objects will run in parallel.
'''

import asyncio, time

async def coroutine(n):
    print(f"coroutine{n}: running")
    await asyncio.sleep(n*2)
    print(f"coroutine{n}: running (sleep over)")
    print("coroutine1: completed")


async def main():
    print("main: running")
    print("\nawaiting tasks (sequential execution) ...")
    c1 = coroutine(1)
    c2 = coroutine(2)
    c3 = coroutine(3)
    await(c1)
    await(c2)
    await(c3)
    time.sleep(2)
    print("\nawaiting coroutines (concurrent execution) ...")
    task1 = asyncio.create_task(coroutine(1))
    task2 = asyncio.create_task(coroutine(2))
    task3 = asyncio.create_task(coroutine(3))
    await task1
    await task2
    await task3
    print("main: running")
    print("main: completed")

asyncio.run(main())     # tasks run concurrently
print()

