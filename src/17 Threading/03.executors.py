'''
As an alternative, you can use a ThreadPoolExecutor to dispatch threads.  Because of the GIL the ThreadPoolExecutor
is best suited to I/O bound tasks, but it can be used with CPU bound tasks as in this example.

The ThreadPoolExecutor manages the worker threads to allow concurrent execution.  You can specify the max number
of concurrent threads (3 in this example).  Use the submit method to pass jobs to the executor.

After each thread completes the ThreadPoolExecutor returns a future object.  As the program progresses we print 
the results from all the futures.
'''

from concurrent.futures import ThreadPoolExecutor
import random, time

JOBS = 10

# define a range offset by 1
def rangex(n):
    return range(1, n+1)

class Worker:
    def __init__(self, n):
        self.n = n
        self.total = 0  # each worker has its own total

    def __call__(self):        
        for n in rangex(self.n):
            time.sleep(random.random() * 0.1)
            self.total += n**2
        return (self.n, self.total)

def main():
    # define a set of jobs for the executor
    jobs = []
    for n in rangex(JOBS):
        job = Worker(n)
        jobs.append(job)

    # create executor and submit all the jobs
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(job) for job in jobs]

        print("\nresults from futures:")

        for future in futures:
            print(future.result(), end=", ")

    print("\nEnd of main")

if __name__ == '__main__': 
    main()
