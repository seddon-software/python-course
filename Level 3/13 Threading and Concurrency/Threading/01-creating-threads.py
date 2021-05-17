############################################################
#
#    creating threads
#
############################################################

import random
import time
import sys

from threading import Thread

def myfunc(name):
    for i in range (1, 50):
        sys.stdout.write(name)        
        time.sleep(random.random() * 0.1)
      

# define a callback function - to be called via start()
thread1 = Thread(target=myfunc, args=("1",))
thread2 = Thread(target=myfunc, args=("2",))
thread3 = Thread(target=myfunc, args=("3",))

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()

print("\nEnd of main Thread") 



