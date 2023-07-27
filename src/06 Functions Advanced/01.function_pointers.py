'''
Function Pointers
=================

Python functions are different from those in other languages.  Let's examine how:

Despite appearances, all Python functions are anonymous.  When we write
            def fib(n):

we are not defining a function called "fib".  What we are doing is creating a pointer called "fib".  This pointer
points at the function object (or the bytecode representing the function).  Pointers in Python can point to
data or to functions.

The line:
            fib(1000)

uses the "fib" pointer to call the function.  However, the next line:
            f = fib

copies the pointer "fib" to another pointer "f".  Now there are two pointers, both pointing at the anonymous
function object.  Now we can invoke the function through either pointer.  Thus
            f(100)
is equivalent to:
            fib(100)

To further emphasise that the function object is anonymous and not directly connected to "fib" we point "fib"
at some totally unrelated data:
            fib = 56.3

Now, the function object is only referenced by "f".  If you try:
            fib(50)
it will throw an exception ('float' object is not callable).  Note,
            print(fib)
will just print 56.3 and not try to call the function object.
'''

def fib(n):  # fib is a pointer to the bytecode
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()

fib(1000)

# create another object reference to the function
f = fib
# call the function through the new object reference
f(100)

# change the original reference
fib = 56.3
print(fib)

# we can still call the function with the new reference
f(50)

# but using fib to call the function won't work because "fib" is now a float
try:
    fib(50)
except Exception as e:
    print(e)



