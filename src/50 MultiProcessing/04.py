'''
The ThreadPoolExecutor class extends the Executor class and returns a Future object.
Executor

The Executor class has three methods to control the thread pool:

    submit() - dispatch a function to be executed and return a Future object. The submit() method takes a function and executes it asynchronously.
    map() - execute a function asynchronously for each element in an iterable.
    shutdown() - shut down the executor.

When you create a new instance of the ThreadPoolExecutor class, Python starts the Executor.
'''

from time import sleep, perf_counter
from concurrent.futures import ThreadPoolExecutor

N = 50

def task(id):
    for _ in range(N):
        print(f'{id}')
        sleep(1)
    return f'Done with task {id}'

start = perf_counter()

with ThreadPoolExecutor() as executor:
    f1 = executor.submit(task, 1)
    f2 = executor.submit(task, 2)

    print(f1.result())
    print(f2.result())    

finish = perf_counter()

print(f"It took {finish-start} second(s) to finish.")
