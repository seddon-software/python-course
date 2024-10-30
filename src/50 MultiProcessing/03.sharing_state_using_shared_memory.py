import os; os.system("clear")
'''
Sharing State using Shared Memory
=================================
Processes can communicate in a variety of ways, but when it comes to sharing large amounts of data, the best option
is to use shared memory.  The shared memory mechanism is very similar on Window, OSX and Linux and the 
multiprocessing module leverages these APIs to provide a consistent mechanism across these operating systems.

Here we present simple examples of using shared memory, but realise this mechanism can support large data volumes.
Shared memory is implemented inside the kernel using virtual memory.  Data doesn't get copied with shared
memory, each process maps the same physical pages into its virtual memory process space.  That way, when one
process changes the shared memory, it is instantaneous seen by all other processes mapped into the same section
of shared memory.

For full details on how shared memory works you should consult blogs online about virtual memory. The API is
written for C programmers and so won't be discussed here.

With Python you define special shared memory variables and Python maps them into shared memory behind the scenes.
Amongst other things you can use 
            (i)  multiprocessing.Value : for scalars
            (ii) multiprocessing.Array : for arrays

Examples of these two mechanisms are given below.  Note that Python creates wrapper objects for "size" and 
"results" and these need casting to see the values stored in shared memory.
'''

import multiprocessing as mp


# this code is executed in a child process, but it modifies shared memory, so the changes can be seen
# by the parent process
def fn(size, results):
    for n in range(size.value):
        results[n] = n*n

if __name__ == '__main__': 
    # mp.Value and mp.Array use shared memory
    size = mp.Value('i', 10)
    results = mp.Array('i', [0]*size.value)

    # expose the wrapper objects
    print(type(size))
    print(type(results))

    p = mp.Process(target=fn, args=(size, results))
    p.start()
    p.join()                # wait for child to complete

    # now view shared memory in parent process
    print(size.value)       # use value attribute to see contents of wrapper object
    print(list(results))    # cast to list to see contents of wrapper object 
