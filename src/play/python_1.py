'''
x = 100;
y = 50
y = x
x = x + 1
'''

from play.xsimulator import *
import os

start()
code = Code(row=2, col=5, lineNumbers=True)
code.set_message_area(20, 20)

stack1 = Stack(row=2, col=30, boxes=2)
stack2 = Stack(row=2, col=50, boxes=3)
thread1 = Thread(2, 3)

x = Variable(name="x", stack=stack1, value="????")
y = Variable(name="y", stack=stack1, value="????")
id_50 = Variable(name="id(50)", stack=stack2, value="50")
id_100 = Variable(name="id(100)", stack=stack2, value="100")
id_101 = Variable(name="id(101)", stack=stack2, value="101")

code(2, "Start of Simulation")
id_100.show_and_print()
x.set("id(100)")
x.show()
x.arrow(id_100)
code(3, " ")
id_50.show_and_print()
y.set("id(50)")
y.show()
y.arrow(id_50)
code(4, " ")
y.set("id(100)")
y.arrow(id_50, hide=True)
x.arrow(id_100)
y.arrow(id_100)
code(5, " ")
x.set("id(101)")
y.arrow(id_100, hide=True)
x.arrow(id_100, hide=True)
y.arrow(id_100)
x.arrow(id_101)
id_101.show_and_print()
code(5, "End of Simulation")
finish()
