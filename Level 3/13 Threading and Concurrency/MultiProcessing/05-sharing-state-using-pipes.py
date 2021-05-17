############################################################
#
#    sharing state between processes
#
############################################################

import multiprocessing as mp

N = 20

def fn(connection, results, N):
    for n in range(N):
        results.append(n*n)
    connection.send(results)

if __name__ == '__main__':
    pipe_parent, pipe_child = mp.Pipe()
    results = []
    p = mp.Process(target=fn, args=(pipe_child, results, N))
    p.start()
    reply = pipe_parent.recv()
    p.join()
    print(reply[:])
    