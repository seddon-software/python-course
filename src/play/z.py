from simulator import *

# loop several times (assume x starts at 30)

program = '''# x = x + 1
# loop several times
LOAD_NAME R1, x
LOAD_CONST R2, 1
BINARY_ADD
STORE_NAME y
# now loop back
'''
start()
colors = Color()
code = Code(row=2, col=5, code=program)

stack1 = Stack(row=2, col=40, boxes=1)
stack2 = Stack(row=2, col=60, boxes=2)
thread1 = Thread(2, 3)
thread2 = Thread(4, 5)
Thread.current_thread = thread1

x = Variable(name="x", stack=stack1, value=30)
R1 = Variable(name="R1", stack=stack2, value=4317012)
R2 = Variable(name="R2", stack=stack2, value=-5132)
R1.show()
R2.show()
R1.print()
R2.print()
x.show()
x.print()

code.step()
for i in range(6):
    code.step()
    R1.set(x)
    code.step()
    R2.set(1)
    code.step()
    R1 += R2
    code.step()
    x.set(R1)
    code.step(-4)
    thread1.swap_colors()
wait()
finish()
