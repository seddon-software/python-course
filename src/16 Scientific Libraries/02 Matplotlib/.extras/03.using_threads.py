'''
Using Threads
=============

Running Matplotlib code in a worker thread is not a good idea.  MatPlotLib creates an event loop in the main 
thread, so all GUI events should be scheduled in this thread.  Furthermore, child artists must be created in the 
same thread as their parent.  In this case 'ax' is a child of 'plt', so both must be created in the main thread.

If you must use a worker thread, since operations on 'ax' are not thread safe, use locks to ensure thread safety.
You will encounter similar problems if you combine MatPlotLib with the asyncio package.
'''

from threading import Thread, Lock
import matplotlib.pyplot as plt

def worker(lock, ax):
    '''
    '''
    lock.acquire() 
    redCircles = "ro"
    ax.plot([1,2,3,4], [1,4,9,16], redCircles)
    ax.set_ylabel("squares")
    lock.release()

lock = Lock()
lock.acquire()
ax = plt.subplot()      # create single figure with one axis
lock.release()
t = Thread(target=worker, args=(lock, ax))
t.start()
t.join()
plt.show()
t.join()




