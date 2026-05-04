'''
With asynchronous programming you are never sure when a calculation has completed.  You can use a futures 
object to wait until a result is available.  Futures effectively contain all the synchronization code 
internally, thus simplifying you code.  

When a coroutine finishes you set the result in the future with: 
            future.set_result(...)

and then examine the result in the calling routine:
            future.result()

The future will not yield the result until the calculation is complete, thus allowing other coroutines to
proceed in the meantime (printDots).  
'''

import asyncio

async def myCoroutine(future, x):
    async def fib(n):
        await asyncio.sleep(0.01)
        await asyncio.create_task(printDots())
        return n if n < 2 else await fib(n-1) + await fib(n-2)
    future.set_result(await fib(x))

async def printDots():
    print(".", end="")
    await asyncio.sleep(0.01)
    
async def main(n):
    future = asyncio.Future()
    await asyncio.create_task(myCoroutine(future, n))

    # retreive result from the future
    print(f"fib({n}) = {future.result()}")

# Start event loop and run until completed
if __name__ == '__main__':
    asyncio.run(main(9))
