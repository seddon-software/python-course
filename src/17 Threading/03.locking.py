'''
Locking
=======

To control parallel threads we can use synchronization classes.  The most import is the "Lock" class.  A "Lock" 
object will allow only one thread at a time execute the code guarded by the lock.  A thread acquires a lock with:
            lock.acquire()

and releases a lock with 
            lock.release()

The code between these calls is guarded.  Such locks are often called monitor locks; they monitor code and only 
allow one thread at a time execute code between the "acquire" and "release" calls.

In this example, 4 threads execute code in the "__call__()" method, but the monitor lock ("lock1") serializes 
execution.

I have provide 4 separate monitor locks so you can experiment with using different locks with different threads.
If you try using two or more locks you will find threads sharing the same lock do not execute concurrently'''

from threading import Thread, Lock
import random
import time
import sys

# create a callable class
class MyClass:
    def __call__(self, name, lock):
        lock.acquire()        
        for i in range (1, 50):
            sys.stdout.write(name)
            time.sleep(random.random() * 0.1)
        lock.release()    

    
lock1 = Lock()
lock2 = Lock()
lock3 = Lock()
lock4 = Lock()

m1 = MyClass()
m2 = MyClass()
m3 = MyClass()
m4 = MyClass()

# give each thread the same lock (try experimenting using the other locks)
t1 = Thread(target = m1, args = ("1", lock1))
t2 = Thread(target = m2, args = ("2", lock1))
t3 = Thread(target = m3, args = ("3", lock1))
t4 = Thread(target = m4, args = ("4", lock1))

# create the worker threads
t1.start()
t2.start()
t3.start()
t4.start()

# wait for the worker threads to finish
t1.join()
t2.join()
t3.join()
t4.join()

print("\nEnd of main")


