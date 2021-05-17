############################################################
#
#    callable classes as callbacks
#
############################################################

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
            time.sleep(random.random() * 0.1)    

    
m1 = MyClass()
m2 = MyClass()
m3 = MyClass()

# define a callback class - __call__() to be called via start()
t1 = Thread(target = m1, args = ("1",))
t2 = Thread(target = m2, args = ("2",))
t3 = Thread(target = m3, args = ("3",))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("\nEnd of main")

1
