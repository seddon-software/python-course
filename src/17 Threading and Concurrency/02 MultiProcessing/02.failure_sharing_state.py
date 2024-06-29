'''
Sharing State
=============
One drawback of using subprocesses is that you can't easily share state (variables).  In this example, we define
a global list called "results" and attempt to populate it from a subprocess.  When you run this program, you
will see the global variable doesn't appear to get updated.

This is because there are 2 global variables! one in each process.  The global variable in the subprocess does
get updated, but we are looking at the second global variable that doesn't get updated.
'''

import multiprocessing as mp


def fn(N):
    for n in range(N):
        results.append(n*n)

results = []        # global state

if __name__ == '__main__': 
    p = mp.Process(target=fn, args=(20,))
    p.start()
    p.join()
    # results will be computed in the child process
    # the parent process doesn't call fn, so results will be empty in the parent process
    print(results)
