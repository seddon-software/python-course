import cothread
from threading import Thread

# in this example, we call a coroutine from a different thread
#  if we try to do this directly, the call will fail
# we have to use cothread.callback instead
def consumer(event):
    while True:
        n = event.Wait()
        print('consumed', n)

import time

def signalViaCallback(n):
    return event.Signal(n)
    
def producer(event, count):
    ''' this is a different thread from that running the cosumer code'''
     
    for n in "ABCDE":
        print('thread tick', n)
        try:
            # can't Signal from a different thread
            if n == "E": event.Signal(n)
        except AssertionError as e:
            print(f"{e}")

        # must use the following to talk across thread boundaries:
        cothread.Callback(signalViaCallback, n)
        time.sleep(0.5)

event = cothread.Event()
cothread.Spawn(consumer, event)
thread = Thread(target=producer, args=(event, 5))
thread.start()
cothread.Sleep(5)
