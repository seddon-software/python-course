'''
try-except-finally
==================
It is often the case that you need to take actions in pairs.  Good examples are opening and closing files, locking
and unlocking a mutex or starting a stopping a timer.  We say this is resource allocation and deallocation.  Bad
things happen if you allocate a resource and forget to deallocate.

Unfortunately, to err is human and programmers often fall into this trap.  This is particularly true when an
unexpected exception occurs.  To help you, Python allows you to define a "finally" block which is guaranteed to
be called even if an exception occurs.

We use the "finally" block to make sure the resource is deallocated.  C++ calls this RAII or Resource Allocation 
is Initialization.  Although this term is frequently used, RAII it has nothing to do with initialization in Python
and is somewhat of a misnomer.

Later in the course we will see Python has a shortcut for RAII; using a "with" statement.

Try running the code twice; once without exception (x = 10) and once when an exception is raised (x = 100).
'''

def f(x):
    print("Locking the mutex")
    if x > 50:
        raise Exception('exception thrown')

try:
    x = 10
    f(x)
except Exception as e:
    print(f'caught exception ... {e}')
else:
    print('no exception thrown')
finally:
    print('finally block is always called ...')
    print("Unlocking the mutex")

print("End of program")

