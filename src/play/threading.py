'''# x = x + 1
# loop several times
LOAD_NAME R1, x
LOAD_CONST R2, 1
BINARY_ADD
STORE_NAME y
# now loop back
'''

from simulator import *
import os

start()
colors = Color()
m = Message(20, 20)
m("Start of Simulation")
code1 = Code(row=2, col=5)
code2 = Code(row=2, col=5)

stack1 = Stack(row=2, col=30, boxes=1)
stack2 = Stack(row=2, col=50, boxes=2)
stack3 = Stack(row=2, col=70, boxes=2)
thread2 = Thread(4, 5)
thread1 = Thread(2, 3)

x = Variable(name="x", stack=stack1, value=30)
R1 = Variable(name="R1", stack=stack2, value="????")
R2 = Variable(name="R2", stack=stack2, value="????")
R3 = Variable(name="R1", stack=stack3, value="????")
R4 = Variable(name="R2", stack=stack3, value="????")
for v in R1, R2, R3, R4, x:
    v.show()
    v.print()
for v in R3, R4:
    thread2.activate()
    v.show()
    v.print()

def incX(thread, code, RA, RB):
    thread.activate()
    code.step()
    while(True):
        code.step()
        RA.set(x)
        code.step()
        RB.set(1)
        code.step()
        RA.set(f"{int(RA.value) + int(RB.value)}")
        code.step()
        yield
        code.step(0)
        x.set(RA)
        code.step(-4)
        yield
        thread.swap_colors()

gen1 = incX(thread1, code1, R1, R2)
gen2 = incX(thread2, code2, R3, R4)

m("Thread 1 starts")
for n in range(7): 
    next(gen1)
m("Thread 1 gets suspended")
m("Thread 2 starts")
for n in range(40): 
    next(gen2)
m("Thread 2 gets suspended")
m("Thread 1 continues")
thread1.activate()
next(gen1)
m("Thread 1 has overwritten x")
m("End of Simulation")
finish()
