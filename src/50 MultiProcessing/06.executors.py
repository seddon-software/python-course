'''
The ThreadPoolExecutor class extends the Executor class and returns a Future object.
Executor

The Executor class has three methods to control the thread pool:

    submit()   - dispatch a function to be executed and return a Future object. 
                 The submit() method takes a function and executes it asynchronously.
    map()      - execute a function asynchronously for each element in an iterable.
    shutdown() - shut down the executor.

When you create a new instance of the ThreadPoolExecutor class, Python starts the Executor.
'''

from time import sleep, perf_counter
from concurrent.futures import ThreadPoolExecutor

def main():
    N = 50

    def task(lo, hi):
        total = 0
        for n in range(lo, hi+1):
            sleep(0.5)
            total += n
        return total


    # use a context manager (with statement) so that the executor shuts down properly
    with ThreadPoolExecutor() as executor:
        future1 = executor.submit(task, 1, 10)
        future2 = executor.submit(task,11, 20)
        future3 = executor.submit(task,21, 30)
        future4 = executor.submit(task,31, 40)
        future5 = executor.submit(task,41, 50)

        # use the executor
        result = future1.result() + future2.result() + future3.result() + future4.result() + future5.result()
        print(f"sum of numbers 1 to 50 = {result}")

    # use sum
    print(f"sum of numbers 1 to 50 = {sum(range(1, 51))}")

if __name__ == '__main__': 
    main()