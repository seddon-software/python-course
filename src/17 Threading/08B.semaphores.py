'''
Here is a similar example that uses Semaphores, but this time we use a ThreadPoolExecutor to dispatch the threads.
After each thread completes the executor returns a future object.  At the end of the example we print the results
from all the futures.
'''

from concurrent.futures import ThreadPoolExecutor
from threading import BoundedSemaphore
import random
import time


THREADS = 25

class MyClass:
    def __init__(self, id):
        self.id = chr(65+id)

    def __call__(self):
        global semaphore
        semaphore.acquire()
        for i in range (1, 50):
            print(self.id, end="")
            time.sleep(random.random() * 0.1)
        semaphore.release()
        return self.id

#lock = mp.Lock()
semaphore = BoundedSemaphore(3)

callbacks = [MyClass(n) for n in range(THREADS)]

with ThreadPoolExecutor() as executor:
    results = [executor.submit(c) for c in callbacks]

print("\nresults from futures:")

for result in results:
    print(result.result(), end=",")

print("\nEnd of main")

