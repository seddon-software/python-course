'''
Global Interpreter Lock
=======================
The GIL is a lock held by CPython interpreter whenever bytecode is being executed unless it is explicitly released 
by the programmer.  CPython assumes that whatever occurs between bytecodes is not thread-safe unless told otherwise.
This implies that the GIL is enabled by default.  CPython releases the GIL periodically to allow other threads to
run.

Other implementations of the Python interpreter such as Jython and IronPython have no GIL and can fully exploit 
multithreading.  PyPy currently has a GIL (similar to CPython) and Cython also has a GIL.  Note, the GIL in Cython 
can be released temporarily using a "with" statement.

After much debate, the Python Steering Council has approved the proposal, PEP 703, "Making the Global Interpreter 
Lock Optional in CPython."  To accomplish this, CPython’s developers will add an experimental “no-GIL” build mode 
to CPython, so that one can compile a version of CPython with or without the GIL. Eventually, the no-GIL build will 
become the default.

In the current versions of CPython (< 14), the GIL is released every few (5) msec by default, but never during a byte code 
instruction.  Thus operations consisting of a single byte code instruction are atomic and hence thread safe.

A thread may release the GIL voluntarily to allow another thread to run.  A thread only needs to hold the GIL 
while it works with Python objects, so CPython will release the GIL and allow another thread to run if the thread
holding the GIL performs I/O operations or other blocking calls.  The GIL may also be released by library code 
written in C/C++.  Note that there is no direct way of releasing the GIL in Python code (but there is if you are 
writing a C/C++ extension).

In the code below we use the dis module to disassemble code for:
            x += 1
            sort([2,5,3,6])

========================================================================================================

x += 1
======

The instruction (x += 1) should always be unsafe because after the byte code instruction to increment x, 
BINARY_OP (+=) there is a further byte code instruction to store x, STORE_NAME.  If the GIL gets released 
between these byte code instructions then another thread could corrupt the value of x.

However, although this was always the case with Python <= 3.9, I've noticed that this doesn't seem to happen
anymore on Python 3.10+ and I'm not sure why.  I can see that one change is that python now uses BINARY_OP
rather than INPLACE_ADD, but this shouldn't change anything.  I've tested this with multiple thread running 
for over 3 hours, but can't get it to go wrong.  Furthermore, you can find several articles on the web that claim 
such code is not thread safe, but these articles are now out of date and don't go wrong anymore (they failed 
in Python 3.9).

On further investigation I've found this behaviour is probably a result of a change that happened with Python 3.11.
This version introduced the "Specializing Adaptive Interpreter".

The “specializing adaptive interpreter” is a standout feature introduced in Python 3.11 and refined in Python 3.12, 
Unlike Python 3.10’s traditional execution model, this fundamentally changes how Python code is executed. Unlike 
Python 3.10’s traditional execution model, which relies on static code paths, the adaptive interpreter dynamically 
adjusts to the behaviour of your code as it runs.  This means it optimizes frequently used operations, adapting on-the-fly to boost performance without requiring any 
changes to your code.  

How the Adaptive Interpreter Works
==================================
    Type Specialization: 
        The interpreter can specialize the bytecode for specific types that it encounters frequently, which allows 
        for faster execution.
    
    Hot Spot Detection: 
        It identifies "hot spots" in the code—sections that are executed frequently—and optimizes them by compiling 
        them into machine code.
    
    Dynamic Optimization: 
        As the program runs, the interpreter adapts to the changing types and execution patterns, allowing it to 
        optimize performance dynamically.

If we use += in a big loop, I believe that the adaptive intepreter doesn't check if it is time to release the GIL 
between the BINARY_OP and STORE_NAME byte code instructions, because of Hot Spot detection or Dynamic Optimization 
- effectively making += thread safe.

Future changes to Python or using a different interpreter (like PyPy) might cause += to fail, so you should still 
use a mutex just in case.

========================================================================================================

sort([2,5,3,6]
==============

Surprisingly, although the second instruction (sort([2,5,3,6])) is quite complicated, it is thread safe.  This is 
because the byte code instructions are all immutable except the call to sort (which can't be interrupted), so the 
code is idempotent and hence thread safe.  Recall that the GIL will not be released in the middle of a byte code 
instruction and hence the BUILD_LIST and CALL_FUNCTION (call to sort) instructions are atomic and hence thread safe.
'''

import dis

dis.dis("x += 1")           # used to be thread unsafe, but now seems to be thread safe (Python 3.10+)
#  1           2 LOAD_NAME                0 (x)
#              4 LOAD_CONST               0 (1)
#              6 BINARY_OP               13 (+=)        # used to be INPLACE_ADD (Python <= 3.10)
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
