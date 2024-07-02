'''
The asyncio module in which these new style coroutines are defined differs from the more traditional threading 
or multiprocess approach to concurrency in that it utilizes an event loop to handle the scheduling of 
asynchronous ‘tasks’ instead of relying on the kernel to perform the scheduling.

Coroutines wrapped as tasks will be executed concurrently inside the event loop.  

Normally we work implicitly with an event loops (see later examples), but here we work with the event loop
explicitly to illustate what is happening more clearly.

Note that all new style coroutine functions must be adorned with the "async" keyword and must be awaited by
their calling coroutine.  To yield control a coroutine has to call:
            asyncio.sleep()

Even sleeping for 0 seconds is sufficient to yield control.
'''

import asyncio
import random

async def worker1():
    while True:
        await asyncio.sleep(random.random()*0.5)
        print("1", end="")

async def worker2():
    while True:
        await asyncio.sleep(random.random()*0.5)
        print("2", end="")

async def worker3():
    while True:
        await asyncio.sleep(random.random()*0.5)
        print("3", end="")

def main():
    loop = asyncio.new_event_loop()
    task1 = loop.create_task(worker1())
    task2 = loop.create_task(worker2())
    task3 = loop.create_task(worker3())

    try:
        print("Hit Ctrl-C to terminate")
        loop.run_forever()    
    except KeyboardInterrupt:
        pass
    finally:
        print("Closing Loop")
        task1.cancel()
        task2.cancel()
        task3.cancel()
        # kill off the tasks safely
        loop.run_until_complete(loop.shutdown_asyncgens())
        loop.close()
        
main()