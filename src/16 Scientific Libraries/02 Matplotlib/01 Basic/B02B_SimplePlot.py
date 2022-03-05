############################################################
#
#    Matplotlib with threads
#
############################################################

from threading import Thread, Lock
import matplotlib.pyplot as plt

'''
Running Matplotlib code in a worker thread is not a good idea.
'''

def worker(lock):
    '''
    MatPlotLib creates an event loop in the main thread, so
    all GUI events must be scheduled in this thread.  Furthermore,
    child artists must be created in the same thread as their parent.
    In this case 'ax' is a child of 'plt', so both must be created in the
    main thread.
    Operations on 'ax' are not thread safe, use locks to ensure thread safety.
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
t = Thread(target=worker, args=(lock,))
t.start()
lock.acquire() 
plt.show()
lock.release()
t.join()




