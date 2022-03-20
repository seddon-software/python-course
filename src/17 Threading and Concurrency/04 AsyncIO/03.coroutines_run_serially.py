'''
Coroutines Run Serially by Default
==================================

In the previous example our coroutines ran concurrently.  However this is not the default behaviour for coroutines;
they need to be made into tasks before they can run in parallel.

In this example we run two separate coroutines, called from the "main()" coroutine, but they are not made into 
tasks.  When you run this example you will see that the coroutines run serially and not concurrently.
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


async def main():
    await coroutineA()
    await coroutineB()

asyncio.run(main())      
