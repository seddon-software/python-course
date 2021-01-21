import asyncio
import time

async def doit(delay):
    # yield immediately
    await asyncio.sleep(delay)
    print(f"message delayed by {delay} secs")

# note this routine runs all doit() calls() concurrently
async def main():
    # schedule tasks
    task1 = asyncio.create_task(doit(2))
    task2 = asyncio.create_task(doit(4))
    task3 = asyncio.create_task(doit(6))

    # this time tasks are run by the scheduler
    # and hence run in parallel and take 6 secs in total
    print(f"started at {time.strftime('%X')}")
    await task1
    print(f"continued at {time.strftime('%X')}")
    await task2
    print(f"continued at {time.strftime('%X')}")
    await task3
    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())

