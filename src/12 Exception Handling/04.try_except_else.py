'''
try-except-else statements
==========================
If an exception is raised, execution is transfered to the "except" clause immediately.  However, if no exception
is raised, excution continues immediately after the "except" block.  Alternatively you can define an "else"
block which will be called in the event of no exception being raised.  The "except" or "else" may contain a
return statement; this will cause a premature exit from the function.   
'''

from math import sqrt
 
def f1():
    try:
        x = int(input("Enter positive integer: "))
        root = sqrt(x)
    except Exception as e:
        print("sqrt() failed ...")
        print(e)
        return
    # after the exception has been handled, execution continues from here unless the exception handler contains
    # a return statement
    print("sqrt() succeeded ...")
    print(root)

def f2():
    try:
        x = int(input("Enter positive integer: "))
        root = sqrt(x)
        print("sqrt() succeeded ...")
        print(root)
    except Exception as e:
        print("sqrt() failed ...")
        print(e)
    # the else block is only executed if no exception is raised
    else:
        print("sqrt() succeeded ...")
        print(root)
    # after the exception has been handled, execution continues from here unless the exception handler or
    # the else block contains a return statement
 
f1()
f2()

