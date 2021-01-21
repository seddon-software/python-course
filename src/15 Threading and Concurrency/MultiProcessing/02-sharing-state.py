############################################################
#
#    sharing state between processes
#
############################################################

import multiprocessing as mp

'''
You can't share state between processes using a global!
'''

results = []        # global state

def fn(N):
    for n in range(N):
        results.append(n*n)

if __name__ == '__main__': 
    p = mp.Process(target=fn, args=(20,))
    p.start()
    p.join()
    # results will be computed in each child process
    # the parent process doesn't call fn, so results will be empty
    print(results)
