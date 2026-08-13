'''
Sharing State using Shared Memory
=================================

Processes can communicate in a variety of ways, but when it comes to sharing large
amounts of data, shared memory can be very efficient.

Shared memory is implemented by the operating system using virtual memory. The
processes map the same physical memory pages into their address spaces. Therefore,
when one process changes the shared memory, another process mapped to the same
memory can see the change without copying the data.

With Python, multiprocessing provides wrapper objects which arrange this shared
memory for us.

Amongst other things:

    multiprocessing.Value : for scalars
    multiprocessing.Array : for arrays

The examples below show both the Python view and the underlying memory.
'''

import multiprocessing as mp
import ctypes
import os


def show_memory(name, results):
    """Display the Python values and the underlying shared memory."""

    # Get the ctypes object containing the actual data
    obj = results.get_obj()

    # Address and size of the actual shared memory
    address = ctypes.addressof(obj)
    size = ctypes.sizeof(obj)

    print()
    print(name)
    print("PID:     ", os.getpid())
    print("Address: ", hex(address))
    print("Size:    ", size, "bytes")
    print("Values:  ", list(results))

    # Read the actual bytes from shared memory
    data = ctypes.string_at(address, size)
    print("Bytes:   ", data.hex())

    # Find the OS memory mapping containing this address
    with open("/proc/self/maps") as f:
        for line in f:
            fields = line.split()

            if not fields:
                continue

            try:
                start, end = [int(x, 16) for x in fields[0].split("-")]
            except ValueError:
                continue

            if start <= address < end:
                print("Mapping: ", line, end="")
                break


# This code is executed in a child process, but it modifies shared memory,
# so the changes can be seen by the parent process.
def fn(size, results):

    show_memory("CHILD BEFORE", results)

    for n in range(size.value):
        results[n] = n * n

    show_memory("CHILD AFTER", results)


if __name__ == '__main__':

    # mp.Value and mp.Array use shared memory
    size = mp.Value('i', 10)
    results = mp.Array('i', [0] * size.value)

    # Expose the wrapper objects
    print("Python wrapper types:")
    print(type(size))
    print(type(results))

    # Show shared memory before the child runs
    show_memory("PARENT BEFORE", results)

    p = mp.Process(target=fn, args=(size, results))
    p.start()
    p.join()                # wait for child to complete

    # Show shared memory after the child has modified it
    show_memory("PARENT AFTER", results)

    print()
    print("size.value =", size.value)
    print("list(results) =", list(results))
    