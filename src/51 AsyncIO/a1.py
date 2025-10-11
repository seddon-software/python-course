'''
Chaining Coroutines
'''

import asyncio
import random
import time

async def main():
    await asyncio.gather(
        *(f1("main") for i in range(3))     # f1 gets scheduled as a task 3 times
    )
async def f1(caller):
    print(f"coroutine: f1({caller=})...")
    print( await f2("f1") )
    print( await f3("f1") )

async def f2(caller):
    print(f"coroutine: f2(caller={caller})...")
    await asyncio.sleep(2)
    return "f2 has finished"

async def f3(caller):
    print(f"coroutine: f3(caller={caller})...")
    await asyncio.sleep(2)
    return "f3 has finished"

if __name__ == "__main__":
    asyncio.run(main())
