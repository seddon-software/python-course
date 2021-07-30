import asyncio
import time

# coroutines do NOT run in parallel by default
# but must be called using await

async def printMessage(delay):
    await asyncio.sleep(delay)
    print(f"message delayed by {delay} secs")

async def main():
    print(f"started at {time.strftime('%X')}")
    await printMessage(2)
    print(f"continued at {time.strftime('%X')}")
    await printMessage(4)
    print(f"continued at {time.strftime('%X')}")

    # calling asyncIO routine without awaiting causes an error
    printMessage(6)
    print(f"finished at {time.strftime('%X')}")

# entry point to async program
asyncio.run(main())
