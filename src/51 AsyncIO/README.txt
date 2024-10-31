1. async IO is a single-threaded, single-process
2. uses cooperative multitasking
3. based around generators (or coroutines)
4. still may need locks for critical sections of code

Asynchronous routines are able to “pause” while waiting on their ultimate 
result and let other routines run in the meantime, thereby facilitating 
concurrent execution.

To install asyncio and aiohttp:
            python -m pip install asyncio --user
            python -m pip install aiohttp --user
