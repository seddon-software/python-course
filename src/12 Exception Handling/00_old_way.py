'''
This is the old way errors were handled in library code.
Note how library routines set a special global variable to indicate an error.
This variable needs to be checked after every call.  This leads to very verbose
coding.

That's not the way to do it!

This style has now been replaced with the more robust exception handling (which
is the subject of this chapter).
'''

errorNo = 0             # special global error indicator

def squareRoot(n):
    if n >= 0:          # n is valid
        errorNo = 0     # reset error code
        return n**0.5   # return result
    else:
                        # n is invalid
        errorNo = 1     # set error code
        return          # don't return anything

def main():
    # first call - OK
    x = squareRoot(10)
    if errorNo == 0:
        print(x)
    else:
        print("error")

    # second call - creates an error
    x = squareRoot(-44)
    if errorNo == 0:
        print(x)
    else:
        print("error")
    
    # third call - OK
    x = squareRoot(20)
    if errorNo == 0:
        print(x)
    else:
        print("error")

