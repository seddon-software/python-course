'''
Callable Classes as Callbacks
=============================

As an alternative to specifying the target function for a thread, we can make the callback function a method in a 
class; this ultimately depends on operator overloading.  In the previous example the callback function was "myfunc" 
and after the "start" method is called, Python calls back on this function.

We can equally specify an object as a callback.  Python will try to call this object; i.e. call the overloaded
() for the class.  Thus if the target is the object "m1" 
            t1 = Thread(target = m1, args = ("1",))

the callback will be on:
            m1()
            
and because of operator overloading, this is equivalent to calling the dunder method:
            m1.__call__()

So you can use an object as the target provided it's class has a "__call__()" method.
'''

from threading import Thread
import random
import time
import sys


# create a callable class
class MyClass:
    def __init__(self):
        pass
    
    def __call__(self, name):
        for i in range (1, 50):
            sys.stdout.write(name) 
            sys.stdout.flush()       
            time.sleep(random.random() * 0.1)    

    
m1 = MyClass()
m2 = MyClass()
m3 = MyClass()

# m1() is equivalent to m1.__call__()
# define a callback target as an object
t1 = Thread(target = m1, args = ("1",))
t2 = Thread(target = m2, args = ("2",))
t3 = Thread(target = m3, args = ("3",))

# create the worker threads
t1.start()
t2.start()
t3.start()

# wait for the worker threads to finish
t1.join()
t2.join()
t3.join()

print("\nEnd of main")

1
