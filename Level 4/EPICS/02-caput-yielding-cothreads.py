import cothread
import random

def worker(n):
    for i in range(25):
        print(f"{n}", end="")
        cothread.Sleep(random.random() * 0.5) # suspend cothread   
    print()

threads = []
for n in range(1, 5):
    t = cothread.Spawn(worker, n)
    threads.append(t)

cothread.Yield()    # wait for other cothreads

# the cothread will terminate when we reach the end of the program
# therefore we must wait for the cothreads to complete
for t in threads:
    t.Wait()
