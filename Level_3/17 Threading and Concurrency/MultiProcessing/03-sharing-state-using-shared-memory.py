############################################################
#
#    sharing state between processes
#
############################################################

import multiprocessing as mp

'''
To share state between processes use: shared memory
(i)  mp.Value : for scalars
(ii) mp.Array : for arrays
'''

# mp.Value and mp.Array use shared memory
size = mp.Value('i', 10)
results = mp.Array('i', [0]*size.value)


def fn(size, results):
    for n in range(size.value):
        results[n] = n*n

if __name__ == '__main__': 
    p = mp.Process(target=fn, args=(size, results))
    p.start()
    p.join()
    # results will be computed in shared memory
    # so the results will be visible to the parent process
    print(results[:])
