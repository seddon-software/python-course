import os; os.system("clear")
'''
We conclude the section with a very brief look at alarms used in asyncio (wait for a period and then 
interrupt).  Note that these alarms include a timeout. 
'''

import asyncio
import time

async def say_after(delay, timeout):
    print(f"waiting for {delay} secs, with timeout of {timeout} secs")
    for _ in range(delay):
        await clock()
    print("hello")

async def clock():
    await asyncio.sleep(1)
    print(".", end="")

timeout = 4
async def main():
    try:
        await asyncio.wait_for(say_after(4, timeout=5), timeout=5)
        await asyncio.wait_for(say_after(7, timeout=10), timeout=10)
        await asyncio.wait_for(say_after(15, timeout=10), timeout=10)
    except asyncio.TimeoutError as e:
        print("timeout", e)
        
asyncio.run(main())

