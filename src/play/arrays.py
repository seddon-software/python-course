'''
#define SIZE 5

void double_array(int myArray[])
{
    for(int i = 0; i < SIZE; i++)
    {
        myArray[i] *= 2;
    }
}

int main(void)
{
    int a[SIZE] = { 100, 200, 300, 400, 500};
    double_array(a);
}
'''

from simulator import *
import os

start()
colors = Color()
m = Message(20, 20)
m("Start of Simulation")
code = Code(row=2, col=5)

stack1 = Stack(row=2, col=50, boxes=2)
stack2 = Stack(row=2, col=80, boxes=5)
thread = Thread(2, 4)

a = []
for i in range(5):
    a.append( Variable(name=f"a[{i}]", stack=stack2, value=f"{100*(i+1)}") )


# start in main
code.step(13)
m("push locals on stack")
code.step(0)

for i in range(5):
    a[i].show()
    a[i].print()
code.step()
thread.swap_colors()

# call function
code.step(-11)
m("push locals on stack")
code.step(0)
myArray = Variable(name="myArray", stack=stack1, value="&a[0]")
myArray.show()
myArray.print()
myArray.arrow(a[0])
code.step(2)
i = Variable(name="i", stack=stack1, value="0")
i.show()
for n in range(5):
    m("push locals on stack")
    i.set(f"{n}")
    code.step(2)
    a[n].set(f"{2*int(a[n].value)}")
    code.step()
    if n == 4: break
    code.step(-3)
code.step()
m("remove locals from stack")
i.hide()
code.step(0)

thread.swap_colors()

# return to main
code.step(5)
m("remove parameters from stack")
myArray.hide()
code.step(0)
code.step()
m("clean up stack")
code.step(0)
for i in range(5):
    a[i].hide()
code.step()

m("End of Simulation")
finish()
