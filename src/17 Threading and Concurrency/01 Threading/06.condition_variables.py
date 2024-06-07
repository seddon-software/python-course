'''
Condition Variables
===================

Apart from locks, there are some other synchronization primatives to consider.  Let's now look at the 
producer/consumer code below.  The problem we have here is that the producer will create data for each of 
the consumers, but it might take some time to do so.  It is important that the consumers don't attempt to 
use the data before it is available.

We can use a "condition" variable to synchronize the threads:
            dataAvailable = threading.Condition()

The consumers all wait on the "condition" variable:
            dataAvailable.wait()

until the producer is ready to provide the data.  The producer notifies all the consumers that they can 
proceed with:
            dataAvailable.notifyAll()
'''

import threading
from threading import Thread
import random
import time
import sys


class Producer:
    def __call__(self, dataAvailable):
        print("Producer is obtaining data - this takes about 10 sec")
        time.sleep(10)
        with dataAvailable:         # grab the lock
            print("Producer is notifying all consumers")
            dataAvailable.notifyAll()

class Consumer:
    def __call__(self, name, dataAvailable):
        with dataAvailable:
            print(f"consumer{name} is waiting")
            dataAvailable.wait()
            print(f"consumer{name} is has obtained the data")


# create condition variable    
dataAvailable = threading.Condition()

producer = Producer()
consumer1 = Consumer()
consumer2 = Consumer()
consumer3 = Consumer()

# give each thread the condition variable
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



