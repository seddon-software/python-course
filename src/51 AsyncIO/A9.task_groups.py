import asyncio
'''
TaskGroup (added in version 3.11) is an asynchronous context manager holding a group of tasks.  All tasks are awaited 
when the context manager exits.  If one task fails then all the other tasks are cancelled (preventing wasted work and 
inconsistent state).  Thus everything is guaranteed to finish or be cancelled.
'''

async def Fib(n):
    async def fib(n):
        await asyncio.sleep(0.00001)
        return n if n < 2 else await fib(n-1) + await fib(n-2)
    result = await fib(n)
    print(f"fib({n}) = {result}")
    return result

async def main():
    async with asyncio.TaskGroup() as task_group:
        task_group.create_task(Fib(23))
        task_group.create_task(Fib(21))
        task_group.create_task(Fib(15))
        task_group.create_task(Fib(7))

asyncio.run(main())
