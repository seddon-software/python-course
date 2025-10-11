'''
Events
======

Event objects are very similar to condition variables.  

The event object is created by:
            event = Event()

and any thread can wait on the event:
            event.wait()

All waiting threads are released when any thread "sets" the event:
            event.set()
'''

from threading import Thread
from threading import Event, Lock
import time

lock = Lock()

class MyClass:
    def __call__(self, name, event):
        print(f"\tthread{name} waiting for event", flush=True)
        event.wait()
        with lock:
            print(f"\tthread{name}  proceeding after event", flush=True)

event = Event()

m1 = MyClass()
m2 = MyClass()
m3 = MyClass()

t1 = Thread(target = m1, args = ("1", event))
t2 = Thread(target = m2, args = ("2", event))
t3 = Thread(target = m3, args = ("3", event))

with lock: print("\nevent has been set in main", flush=True)
t1.start()
t2.start()
t3.start()

with lock: print("\nmain waiting for 10 seconds", flush=True)
time.sleep(10)
print("main clearing event flag")
event.set()

