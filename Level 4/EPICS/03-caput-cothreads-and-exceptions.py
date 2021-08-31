import cothread
import random

def worker(n):
    for i in range(25):
        print(f"{n}", end="")
        if i == 6: 
            raise Exception(f"cothread {n} crashed!")
        cothread.Sleep(random.random() * 0.5) # suspend cothread   

    print()

threads = []
for n in range(1, 5):
    # report crashes to main cothread
    t = cothread.Spawn(worker, n, raise_on_wait=True)
    threads.append(t)

cothread.Yield()    # wait for other cothreads

for t in threads:
    try:    # check if cothreads raise an exception
        t.Wait()    
    except Exception as e:
        print(e)
