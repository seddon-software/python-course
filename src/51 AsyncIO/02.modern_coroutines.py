'''
    A coroutine function is declared as:
            async def coroutine_function(): ...

    A coroutine object is returned from the call to a coroutine function.
    You await coroutine objects, not coroutine functions.

    await causes the current coroutine function to suspend and delegates execution of the awaitable 
    coroutine object to the event loop, which will schedule it as needed.

    A coroutine yields control when it awaits another coroutine object,

    All coroutine functions must be defined using the `async` keyword. A coroutine must be awaited by another 
    coroutine (or run by an appropriate event loop).  To suspend a coroutine and yield control to the event loop, 
    use `await`. For example:

        await asyncio.sleep(1)

    While the coroutine is suspended, the event loop can run other tasks.
    Even sleeping for 0 seconds is sufficient to yield control.
'''

import asyncio


async def coroutine_function():
    await  asyncio.sleep(0.1)       # yield control

    coroutine_object = asyncio.sleep(0.1) 
    await coroutine_object          # yield control

async def main():
    coroutine_object = coroutine_function()
    print(coroutine_function)
    print(coroutine_object)
    await coroutine_object          # yield control
asyncio.run(main())
