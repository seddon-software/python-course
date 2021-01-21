import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


timeout = 4
async def main():
    try:
        await asyncio.wait_for(say_after(1, "waiting for 1 sec"), timeout)
        await asyncio.wait_for(say_after(3, "waiting for 3 sec"), timeout)
        await asyncio.wait_for(say_after(5, "waiting for 5 sec"), timeout)
    except asyncio.TimeoutError as e:
        print("timeout", e)
        
asyncio.run(main())

