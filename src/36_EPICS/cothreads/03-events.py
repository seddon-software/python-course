import cothread
import random

def worker(n, event):
    event.Wait()
    for i in range(25):
        print(f"{n}", end="")
        cothread.Sleep(random.random() * 0.5) # suspend cothread   
    print()

threads = []
event = cothread.Event(auto_reset=False)
# auto_reset=True:  let only one cothread see the signal
# auto_reset=False: let all cothreads see the signal

for n in range(1, 5):
    t = cothread.Spawn(worker, n, event)
    threads.append(t)

delay = 10
print(f"main cothread waiting for {delay} seconds")
cothread.Sleep(delay)

event.Signal()
for t in threads:
    t.Wait()    
