'''
Global Interpreter Lock
=======================
The GIL is a lock held by CPython interpreter whenever bytecode is being executed unless it is explicitly released 
by the programmer.  CPython assumes that whatever occurs between bytecodes is not thread-safe unless told otherwise.
This implies that the GIL is enabled by default.  CPython releases the GIL periodically to allow other threads to
run.

Other implementations of the Python interpreter such as Jython and IronPython have no GIL and can fully exploit 
multithreading.  PyPy currently has a GIL (similar to CPython) and Cython also has a GIL.  Note, the GIL in Cython 
can be released temporarily using a "with" statement. The latest releases of CPython do have an option to diexperimental

After much debate, the Python Steering Council intends to approve a proposal, PEP 703, "Making the Global Interpreter 
Lock Optional in CPython."  To accomplish this, CPython’s developers will add an experimental “no-GIL” build mode 
to CPython, so that one can compile a version of CPython with or without the GIL. Eventually, the no-GIL build will 
become the default.

In the current version of CPython, the GIL is released every few (<10) msec, but never during a byte code instruction.
Thus operations consisting of a single byte code instruction are atomic and hence thread safe.

A thread may release the GIL voluntarily to allow another thread to run.  A thread only needs to hold the GIL 
while it works with Python objects, so CPython will release the GIL and allow another thread to run if the thread
holding the GIL performs I/O operations or other blocking calls into the OS like select() and pthread_mutex_lock().
The GIL may also be released by library code written in C/C++.  Note that there is no direct way of releasing the 
GIL in Python code (but there is if you are writing a C/C++ extension).

In the code below we use the dis module to disassemble code for:
            x += 1
            sort([2,5,3,6])

Note that the first instruction (x += 1) consists of several byte code instructions including only one mutable
byte code instruction (BINARY_OP) and hence is thread safe.  In releases of Python < 3.10 this code expanded to several
mutable byte code instructions and was not thread safe.  You can find several articles on the web that claim this is not thread
safe, but these articles are now out of date.  In the next example in this chapter we will look at some code that does have 
several mutable byte code instructions that is not thread safe. 

Surprisingly, although the second instruction (sort([2,5,3,6])) is quite complicated, it is thread safe.  This is 
because the byte code instructions are all immutable except the call to sort (which can't be interrupted), so the code is 
idempotent and hence thread safe.  Recall that the GIL will not be released in the middle of a byte code instruction and 
hence the BUILD_LIST and CALL_FUNCTION (call to sort) 
instructions are atomic and hence thread safe.
'''

import dis

dis.dis("x += 1")           # used to be thread unsafe, but now is thread safe
#  1           2 LOAD_NAME                0 (x)
#              4 LOAD_CONST               0 (1)
#              6 BINARY_OP               13 (+=)
#             10 STORE_NAME               0 (x)
#             12 LOAD_CONST               1 (None)
#             14 RETURN_VALUE
#  0           0 RESUME                   0

dis.dis("sort([2,5,3,6])")  # thread safe
#  1           2 PUSH_NULL
#              4 LOAD_NAME                0 (sort)
#              6 BUILD_LIST               0
#              8 LOAD_CONST               0 ((2, 5, 3, 6))
#             10 LIST_EXTEND              1
#             12 PRECALL                  1
#             16 CALL                     1
#             26 RETURN_VALUE