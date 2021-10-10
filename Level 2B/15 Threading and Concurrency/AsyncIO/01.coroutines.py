import asyncio

# this is a coroutine (related to a generator)
async def main():
    print('hello')
    await asyncio.sleep(1)
    print('world')


print(main)             # main is a function

c = main()              # calling main creates a coroutine, but doesn't run it
asyncio.run(c)          # this schedules the coroutine to run

# or more simply
asyncio.run(main())
