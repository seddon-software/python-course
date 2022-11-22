import cothread
import random


def callback():
    print(f"\ncallback\n")

cothread.Timer(5, callback, retrigger=True)

for n in range(100):
    cothread.Sleep(0.5)  
    print(n, end=", ")
