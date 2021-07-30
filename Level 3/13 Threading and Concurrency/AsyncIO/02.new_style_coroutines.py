import asyncio

# this is a new style coroutine
async def main():
    print('hello', end=" ")
    await asyncio.sleep(1)
    print('world')

cr = main()              # calling main creates a coroutine, but doesn't run it
print(type(cr))

asyncio.run(cr)          # this schedules the coroutine to run
# or more simply
asyncio.run(main())
