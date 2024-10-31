import os; os.system("clear")
'''
Sharing State using Queues
==========================
You can use queues as an alternative to shared memory.  Queues use FIFOs between processes rather than shared 
memory, but the result is much the same.

In this example we use queues to calculate the squares of the first N integers in a child process and print
the results from the parent process.
'''

import multiprocessing as mp


# this code is executed in a child process, but it uses FIFOs, so the changes can be seen by the parent process
def fn(q, results, N):
    for n in range(N):
        results.append(n*n)
    q.put(results)

if __name__ == '__main__':
    N = 20    # number of integers to process
    results = []
    q = mp.Queue()

    # create child process and pass it the queue
    p = mp.Process(target=fn, args=(q, results, N))
    p.start()
    p.join()                # wait for child to complete

    # now view results in parent process
    print(q.get())
    
