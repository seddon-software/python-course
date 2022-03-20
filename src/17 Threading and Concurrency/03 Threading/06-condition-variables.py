############################################################
#
#    locking
#
############################################################

import threading
from threading import Thread
import random
import time
import sys


class Producer:
    def __call__(self, dataAvailable):
        print("Producer is obtaining data")
        time.sleep(5)
        with dataAvailable:         # grab the lock
            print("Producer is notifying all consumers")
            dataAvailable.notifyAll()

class Consumer:
    def __call__(self, name, dataAvailable):
        with dataAvailable:
            print(f"consumer{name} is waiting")
            dataAvailable.wait()
            print(f"consumer{name} is has obtained the data")

    
dataAvailable = threading.Condition()

producer = Producer()
consumer1 = Consumer()
consumer2 = Consumer()
consumer3 = Consumer()

# give each thread a lock
t = Thread(target = producer, args = (dataAvailable,))
t1 = Thread(target = consumer1, args = ("1", dataAvailable))
t2 = Thread(target = consumer2, args = ("2", dataAvailable))
t3 = Thread(target = consumer3, args = ("3", dataAvailable))

t.start()
t1.start()
t2.start()
t3.start()

t.join()
t1.join()
t2.join()
t3.join()

print("\nEnd of main")


