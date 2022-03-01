'''
Default Parameters
==================

Another useful feature of functions is that you can use defaults for some parameters.  The display function below,
or rather the anonymous function pointed at by the "display" pointer allows us to use defaults for a and b.

Then,      display(17)      is equivalent to     display(17, 10, 100)   since the parameters b and c are defaulted.  
Similarly  display(17, 21)  is equivalent to     display(17, 21, 100)
Finally,   display(17, c=0) is equivalent to     display(17, b=10, c=0) or display(17, 10, c=0)

You can even list the defaults of the function object with "display.__defaults__"
'''    

def display(a, b=10, c=100):
    print(f"a = {a:6.2f}, b = {b:6.2f}, c = {c:6.2f}")

display(a=19, b=-6.2, c=4.8)
display(b=-6.2, c=4.8, a=19 )
display(17)
display(17, 21)
display(17, c=0)
print(display.__defaults__)
