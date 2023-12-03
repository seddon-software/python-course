'''
Global Interpreter Lock
=======================
The GIL is a lock held by CPython interpreter whenever bytecode is being executed unless it is explicitly released 
by the programmer.  CPython assumes that whatever occurs between bytecodes is not thread-safe unless told otherwise.
This implies that the GIL is enabled by default.  CPython releases the GIL periodically to allow other threads to
run.

Other implementation of the Python interpreter such as Jython and IronPython have no GIL and can fully exploit 
multithreading.  PyPy currently has a GIL (similar to CPython) and Cython also has a GIL.  Note, the GIL in Cython 
can be released temporarily using a "with" statement. 

In CPython, the GIL is released every few (<10) msec after completing a byte code instruction.  Operations 
consisting of a single byte code instruction are atomic and hence thread safe.

A thread may release the GIL voluntarily to allow another thread to run.  A thread only needs to hold the GIL 
while it works with Python objects, so CPython will release the GIL and allow another thread to run if the thread
holding the GIL performs I/O operations or other blocking calls into the OS like select() and pthread_mutex_lock().
The GIL may also be released by library code written in C/C++.  Note that there is no direct way of releasing the 
GIL in Python code (but there is if you are writing a C/C++ extension).

In the code below we use the dis module to disassemble code for:
            x += 1
            sort([2,5,3,6])

Note that the first sequence is mutable and hence not thread safe.  If we are suspended after INPLACE_ADD then
we would overwrite any work performed by other threads executing the same code.

Surprisingly, although the second sequence is more complicated, it is thread safe.  This is because the byte code
instructions are all immutable, so the code is idempotent and hence thread safe.  Recall that the GIL will not be 
released in the middle of a byte code instruction and hence the BUILD_LIST and CALL_FUNCTION (call to sort) 
instructions are atomic and hence thread safe.
'''

import dis

dis.dis("x += 1")           # not thread safe
#               0 LOAD_NAME                0 (x)
#               2 LOAD_CONST               0 (1)
#               4 INPLACE_ADD
#               6 STORE_NAME               0 (x)

dis.dis("sort([2,5,3,6])")  # thread safe
#               0 LOAD_NAME                0 (sort)
#               2 LOAD_CONST               0 (2)
#               4 LOAD_CONST               1 (5)
#               6 LOAD_CONST               2 (3)
#               8 LOAD_CONST               3 (6)
#              10 BUILD_LIST               4            <== ATOMIC
#              12 CALL_FUNCTION            1            <== ATOMIC
#              14 RETURN_VALUE