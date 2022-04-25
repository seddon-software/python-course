from simulator import *
import os

program = '''
int x = 100;
int* px;
px = &x;
printf("%i\\n", *px);
'''

start()
colors = Color()
message(12, 20, "Start of Simulation")
code = Code(row=2, col=5, code=program)

stack1 = Stack(row=2, col=30, boxes=1)
stack2 = Stack(row=2, col=50, boxes=1)
thread1 = Thread(2, 3)

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
arrow(px, x)
code.step()
message(12, 20, "100")
code.step()
message(12, 20, "End of Simultion")
finish()
