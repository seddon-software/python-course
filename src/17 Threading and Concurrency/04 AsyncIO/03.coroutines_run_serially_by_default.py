'''
Coroutines Run Serially by Default
==================================

In the previous example our coroutines ran concurrently.  However this is not the default behaviour for coroutines;
they need to be wrapped as a task before they can run in parallel.  Needless to say, the default behaviour is
unesirable; we want to run the coroutines concurrently.

In this example we run three separate coroutines, called from the "main()" coroutine, but they are not made into 
tasks.  When you run this example you will see that the coroutines run serially and not concurrently.

Compare this with "main2()" where we wrap the same coroutines as tasks and this time they do run concurrently.
'''

import asyncio

# this is a new style coroutine
async def coroutineA():
    print('I am coroutineA')
    await asyncio.sleep(1)                # yield control
    print('I am coroutineA')

async def coroutineB():
    print('I am coroutineB')
    await asyncio.sleep(1)                # yield control
    print('I am coroutineB')

async def coroutineC():
    print('I am coroutineC')
    await asyncio.sleep(1)                # yield control
    print('I am coroutineC')


async def main():
    await coroutineA()
    await coroutineB()
    await coroutineC()

async def main2():
    taskA = asyncio.create_task(coroutineA())
    taskB = asyncio.create_task(coroutineB())
    taskC = asyncio.create_task(coroutineC())

asyncio.run(main())      
asyncio.run(main2())      
