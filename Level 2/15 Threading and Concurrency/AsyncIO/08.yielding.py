import asyncio
import time
import types

# use yield, yield from inside coroutines that are not async generators

def f():
    time.sleep(1)
    yield
    return

@asyncio.coroutine
def aaa():
    print("aaa")
    print("aaa")
    print("aaa")
    yield from f()
    print("aaa")
    print("aaa")
    print("aaa")

@asyncio.coroutine
def bbb():
    print("bbb")
    print("bbb")
    print("bbb")
    yield from f()
    print("bbb")
    print("bbb")
    print("bbb")

async def main():
    task1 = asyncio.create_task(aaa())
    task2 = asyncio.create_task(bbb())

    print(f"started at {time.strftime('%X')}")
    # Wait until both tasks are completed
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())
