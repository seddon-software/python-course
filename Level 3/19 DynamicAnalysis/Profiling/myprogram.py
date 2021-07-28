import random, time

count = 0
n = 100
def f1():
    global count
    for i in range(n):
        sleepy()
        count = count + i

def f2():
    global count
    for i in range(2 * n):
        sleepy()
        count = count + i

def f3():
    global count
    for i in range(3 * n):
        sleepy()
        count = count + i

def f4():
    global count
    for i in range(4 * n):
        sleepy()
        count = count + i

def sleepy():
    sleep1()
    sleep2()
    sleep3()
    
def sleep1():
    time.sleep(random.random() * 0.001)
def sleep2():
    time.sleep(random.random() * 0.002)
def sleep3():
    time.sleep(random.random() * 0.003)
def foo():
    f1()
    f2()
    f3()
    f4()
    
