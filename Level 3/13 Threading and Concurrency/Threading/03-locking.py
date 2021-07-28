############################################################
#
#    locking
#
############################################################

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

# give each thread a lock
t1 = Thread(target = m1, args = ("1", lock1))
t2 = Thread(target = m2, args = ("2", lock2))
t3 = Thread(target = m3, args = ("3", lock3))
t4 = Thread(target = m4, args = ("4", lock3))

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()

print("\nEnd of main")

1
