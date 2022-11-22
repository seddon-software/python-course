import cothread
import random

queue = cothread.EventQueue()

def producer(queue):
    for i in range(25):
        cothread.Sleep(random.random() * 1.5)
        print(f'item produced: {i}')
        queue.Signal(i)

def consumer(queue):
    for item in queue:
        cothread.Sleep(random.random() * 0.5)
        print(f'item consumed: {item}')

c = cothread.Spawn(consumer, queue)
p = cothread.Spawn(producer, queue)


cothread.Sleep(10)

c.Wait()
p.Wait()
