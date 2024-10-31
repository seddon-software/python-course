import os; os.system("clear")
'''
Coroutines run serially by default; they need to be wrapped as a task before they can be run in parallel.  
Needless to say, this default behaviour is unesirable; we want to run the coroutines concurrently.

Here we work with an implicit event loop.  The asyncio event loop is created with
            asyncio.run(main())
or
            asyncio.run(main2())
            
In this example we run three separate coroutines, called from the "main()" coroutine, but they are not made 
into tasks.  When you run this example you will see that the coroutines run serially and not concurrently.

Compare this with "main2()" where we wrap the same coroutines as tasks and this time they do run concurrently.
'''

import asyncio
import random

N = 20
def delay():
    return random.random()*0.5

async def coroutine1():
    for n in range(N):
        print('1', end="")
        await asyncio.sleep(delay())                # yield control

async def coroutine2():
    for n in range(N):
        print('2', end="")
        await asyncio.sleep(delay())                # yield control

async def coroutine3():
    for n in range(N):
        print('3', end="")
        await asyncio.sleep(delay())                # yield control



async def main():
    await coroutine1()
    await coroutine2()
    await coroutine3()

async def main2():
    task1 = asyncio.create_task(coroutine1())
    task2 = asyncio.create_task(coroutine2())
    task3 = asyncio.create_task(coroutine3())
    await task1
    await task2
    await task3

print("\nawaiting coroutines")
asyncio.run(main())      # coroutines run serially
print("\nawaiting tasks")
asyncio.run(main2())     # tasks run concurrently
print()

