'''
#define SIZE 5

void double_array(int* myArray)
{
    for(int i = 0; i < SIZE; i++)
    {
        myArray[i] *= 2;
        myArray++;
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
stack2 = Stack(row=2, col=80, boxes=6)
thread = Thread(2, 4)

a = []
for i in range(5):
    a.append( Variable(name=f"a[{i}]", stack=stack2, value=f"{100*(i+1)}") )
dummy = Variable(name=f"", stack=stack2, value=f"{100*(i+1)}")  # end of stack


# start in main
code.step(14)
m("push locals on stack")
code.step(0)

for i in range(5):
    a[i].show()
    a[i].print()
code.step()
m("call function and push parameter on stack")
code.step(0)
myArray = Variable(name="myArray", stack=stack1, value="&a[0]")
myArray.print()
myArray.arrow(a[0])
code.step(0)

# call function
myArray.show()
thread.swap_colors()
code.step(-12)
m("push locals on stack")
code.step(2)
i = Variable(name="i", stack=stack1, value="0")
i.show()
m("push locals on stack")
for n in range(5):
    code.step(0)
    i.set(f"{n}")
    code.step(2)
    a[n].set(f"{2*int(a[n].value)}")
    code.step()
    myArray.set(f"&a[{n+1}]")
    myArray.arrow(a[n], True)
    if n == 4: break
    myArray.arrow(a[n+1])
    code.step(-3)
myArray.arrow(dummy)
code.step()
m("pop i on exit from stack frame")
code.step(0)
i.hide()
code.step()

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
