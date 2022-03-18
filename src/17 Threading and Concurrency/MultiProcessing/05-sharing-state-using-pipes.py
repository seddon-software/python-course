'''
Sharing State using Pipes
=========================
Although queues
For passing messages between multiple processes you can use Queues.  For passing messages between two processes
you can use a Pipe().

Here is the previous example, rewritten using a pipe.
'''

import multiprocessing as mp


# this code is executed in a child process, but it uses pipes, so the changes can be seen by the parent process
def fn(connection, results, N):
    for n in range(N):
        results.append(n*n)
    connection.send(results)

if __name__ == '__main__':
    N = 20    # number of integers to process
    results = []

    # create the two ends of the pipe
    pipe_parent, pipe_child = mp.Pipe()

    # create child process and pass one end of the pipe
    p = mp.Process(target=fn, args=(pipe_child, results, N))
    p.start()
    p.join()                # wait for child to complete

    # now view results in parent process
    reply = pipe_parent.recv()
    print(list(reply))
    