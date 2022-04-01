############################################################
#
#    sharing data
#
############################################################

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
        def progress(v):
            M = N//50
            if i%M == 0 and i!=0:
                print(f"{int(i/M) + (v-1)*50}% ", end="", flush=True)
        
        if name == "A":
            for i in range(0, N):
                M.count1 += 1
                progress(1)
            M.lock.acquire()
            for i in range(0, N):
                M.count2 += 1
                progress(2)
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

