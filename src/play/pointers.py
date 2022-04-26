'''
int x = 100;
int* px;
px = &x;
printf("%i\\n", *px);
'''

from simulator import *
import os

start()
colors = Color()
m = Message(12, 20)
m("Start of Simulation")
code = Code(row=2, col=5)

stack1 = Stack(row=2, col=30, boxes=1)
stack2 = Stack(row=2, col=50, boxes=1)
thread = Thread(2, 3)

x = Variable(name="x", stack=stack2, value="????")
px = Variable(name="px", stack=stack1, value="????")
x.show()
x.print()

code.step()
x.set(100)
code.step()
px.show()
px.print()
code.step()
px.set("&x")
px.arrow(x)
code.step()
m("100")
code.step()
m("End of Simultion")
finish()
