'''
Creating Threads
================

Question: What is a Thread?

A thread is a separate flow of execution through your code. This means that different threads may be running the 
same code at different times, but they could be executing entirely different code.

Threads are used when you want to run multiple sections of code concurrently.  In most programming languages, 
threads can be run on different CPUs to achieve true concurrency, but often time slicing on the same CPU is used 
to create apparent concurrency.  When multiple CPUs are used, threading can greatly speed up code.

Most Python programs are run using CPython which is the default implementation of Python.  CPython was originally
written when single threaded programs were the norm and it was felt that making CPython thread safe (see later
for what that really means) would slow down existing programs.  To avoid contentions between threads, CPython 
creates a Global Interface Lock (GIL) each time a thread is run, effectively serialising threaded code.  
Although this avoids errors it also creates a performance bottleneck; we will look at the GIL in subsequent 
examples.  Many attempts have been made to make CPython thread safe, but so far none has been accepted by the 
Python community.  However this is changing; the proposal PEP 703: "Making the Global Interpreter Lock Optional 
in CPython" has now been accepted and Python 3.13 has a working implementation of this PEP.

In previous version of Python, threading is still useful for concurrent tasks, but your code won't necessarily 
run faster.  IO-bound tasks spend a lot of time waiting (idle) for data to be ready.  For these tasks there is 
a real speed benefit by switching to running code in another thread when the the current thread becomes I/O 
bound.  However, for CPU-bound tasks, switching threads won't speed things up because no threads are in an idle 
state.

Note that libraries written in C/C++ such as Numpy bypass the GIL and can use threading for CPU-bound tasks.

If you want to run concurrent CPU-bound Python code, you should check out the multiprocessing module instead.
This gets around the problem of using the GIL by creating separate python interpreters, one for each process.

Recall that threads are used to perform concurrent tasks.  Threads are ultimately created by the operating 
system (kernel), but as far as we are concerned we just make a Python call to start a thread; the Python 
interpreter then contacts the kernel on our behalf.  Python provides a helper class to manage threads.  Rather 
confusingly, this class is called "Thread".  Objects of this class are NOT threads, just helper objects!

All programs start with a single thread (aka the main thread).  When the main thread wants to create further 
threads, it creates objects of the helper class and calls their "start" method:
            thread1.start()
            thread2.start()
            thread3.start()

Realize that when the new threads start, they need to perform a different task (or function) from the main 
thread.  This task is specified as a parameter ("target") when the main thread creates the helper objects:
            thread1 = Thread(target=myfunc, args=("1",))
            thread2 = Thread(target=myfunc, args=("2",))
            thread3 = Thread(target=myfunc, args=("3",))

Creating the helper objects DOES NOT create any threads - calling the start method creates and starts a thread.  
After the "start" method has been called, execution of the main thread and the other threads continues in 
parallel.  Because the operating system may suspend threads at any time, it is not possible to predict which 
order code will execute in different threads unless we use special synchronization objects.

In this example the main thread creates 3 other (worker) threads which all execute the "myfunc" function.  
Each of these threads terminate when they complete this function.  I've added some random delays to emphasize 
the parallel nature of this program.

The "join()" methods are executed by the main thread to wait for each worker thread to complete in turn, 
ensuring the main thread finishes last.  If you don't use "join()" and the main thread finishes, then 
the other threads run to completion.  Alternatively you can mark threads as daemons and they will terminate
prematurely when the main thread exits.

To set the thread as a daemon thread use:
    thread.daemon = True
'''

import random
import time
import sys
from threading import Thread

def myfunc(name):
    for i in range (1, 50):
        sys.stdout.write(name)        
        time.sleep(random.random() * 0.1)
      

# define a callback function as the target - to be called via start()
t1 = Thread(target=myfunc, args=("1",))
t2 = Thread(target=myfunc, args=("2",))
t3 = Thread(target=myfunc, args=("3",))

# create the worker threads
t1.start()
t2.start()
t3.start()

print("\nEnd of main Thread") 



