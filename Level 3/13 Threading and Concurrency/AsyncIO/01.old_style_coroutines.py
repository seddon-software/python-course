import asyncio
import time

# this is a coroutine (related to a generator)

def main():
    print('hello', end=" ")
    time.sleep(1)
    yield
    print('world')

cr = main()              # calling main creates a coroutine, but doesn't run it
print(type(cr))

asyncio.run(cr)          # this schedules the coroutine to run
# or more simply
asyncio.run(main())
