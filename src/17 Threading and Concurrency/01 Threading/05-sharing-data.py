'''
Sharing Data
============
As discussed previously, code using += is not thread safe.  As an illustration of this we define two counts and
then increment these counts in 3 separate threads.  One of the counts is protected by a lock, but the other is not.
We have to increment many (10 million) times to maximise the chance of being suspended in the critical section of 
code.  The protected count will always end up at 3 threads x 10 million = 30,000,000, but the other count will
usually end up less as a result of the contention between the threads.

Because programmers are prone to forget to release locks, we give alternate ways of using a lock in threads "B"
and "C".  Thread "B" uses a finally block and thread "C" uses a with statement.  The "with" statement is expanded
by the interpreter to the try-finally form (so these forms are equivalent).

Note that often code is modified after the initial design and we might introduce code that could throw an exception
between obtaining the lock and releasing it.  That's why it's better to use the with statement than the straight
lock.release() because "with" is exception safe.
'''

from threading import Thread
from threading import Lock

# 3 threads increment 2 Counters ...
# count1 is unprotected
# count2 is protected

N = 10*1000*1000

class M:
    lock = Lock()
    count1 = 0
    count2 = 0

    def __call__(self, name):                
        if name == "A":
            for i in range(0, N):
                M.count1 += 1
            M.lock.acquire()
            for i in range(0, N):
                M.count2 += 1
            M.lock.release()
        if name == "B":
            for i in range(0, N):
                M.count1 += 1
            M.lock.acquire()
            try:
                for i in range(0, N):
                    M.count2 += 1
            finally:
                M.lock.release()
        if name == "C":
            for i in range(0, N):
                M.count1 += 1
            with M.lock:
                for i in range(0, N):
                    M.count2 += 1

m1 = M()
m2 = M()
m3 = M()

t1 = Thread(target = m1, args = ("A",))
t2 = Thread(target = m2, args = ("B",))
t3 = Thread(target = m3, args = ("C",))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("")
print(f"M.count1: {M.count1}")
print(f"M.count2: {M.count2}")

