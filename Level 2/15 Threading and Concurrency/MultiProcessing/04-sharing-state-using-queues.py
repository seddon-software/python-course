############################################################
#
#    sharing state between processes
#
############################################################

import multiprocessing as mp

N = 20

def fn(q, results, N):
    for n in range(N):
        results.append(n*n)
    q.put(results)

if __name__ == '__main__':
    results = []
    q = mp.Queue()
    p = mp.Process(target=fn, args=(q, results, N))
    p.start()
    print(q.get())
    p.join()
    