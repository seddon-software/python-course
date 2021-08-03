import asyncio
import time

async def task(id):
    for i in range(10):
        await asyncio.sleep(0)
        print(f"{id}", end="")

# note main() runs all calls concurrently
async def main():
    tasks = []

    # schedule tasks
    for id in range(1, 10):
        t = asyncio.create_task(task(f"{id}"))
        tasks.append(t)

    # schedule tasks
    for t in tasks:
        await t
    print()
    
asyncio.run(main())

