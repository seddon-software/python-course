'''
When you await a coroutine object it will get scheduled immediately and run to completion.
If you do this with several coroutine objects you will find they are each run to completion in turn and not run
in parallel.

However, if you wrap a coroutine object inside a task it gets scheduled and put into a pending state.  
If you do this with several coroutine objects they will all be scheduled in a pending state.
Now when any task is awaited the coroutine objects will run in parallel.
'''

import asyncio, time

async def coroutine1(n):
    print(f"{coroutine1.__name__}: running")
    await asyncio.sleep(3)
    print("coroutine1: running (sleep over)")
    print("coroutine1: completed")

async def coroutine2(n):
    print("coroutine2: running")
    await asyncio.sleep(6)
    print(f"coroutine2: running (sleep over)")
    print(f"coroutine2: completed")

async def coroutine3(n):
    print("coroutine3: running")
    await asyncio.sleep(6)
    print(f"coroutine3: running (sleep over)")
    print(f"coroutine3: completed")

async def main():
    print("main: running")
    print("\nawaiting tasks (sequential execution) ...")
    c1 = coroutine1(6)
    c2 = coroutine2(4)
    c3 = coroutine3(2)
    await(c1)
    await(c2)
    await(c3)
    time.sleep(2)
    print("\nawaiting coroutines (concurrent execution) ...")
    task1 = asyncio.create_task(coroutine1(6))
    task2 = asyncio.create_task(coroutine2(4))
    task3 = asyncio.create_task(coroutine3(2))
    await task1
    await task2
    await task3
    print("main: running")
    print("main: completed")

asyncio.run(main())     # tasks run concurrently
print()

