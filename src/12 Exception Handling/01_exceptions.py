'''
Exceptions
==========
Exceptions were introduced into programming languages in the 70s and became mainstream when they were added
to C++ in the early 90s.  C++ used the terms
            try throw catch

However, when exceptions were added to Python, the following keywords were used:
            try raise except

In early programming languages you had to check return codes from function calls to see if the function failed.
For example, a square root function might return -1 on error (when taking the square root og a negative number).
Checking return codes leads to cluttered code and is tedious to implement consistently, to such an extent that
programmers often didn't check return codes at all.

All of this led to buggy code; exception handling takes a more robust approach.  Instead of the programmer checking
return, we get the language to add error checking whenever we add a "try" block.  Exception handling still has
some problems, but overall is a much better design.

Try playing around with values of x below, to see exceptions being raised:
            raise Exception("x is much too big")
and caught in an exception handler:
            except Exception as e:
                print(e)

Note that:
            Exception("x is much too big")

creates an anonymous object of type Exception.  To interact with this object we need a reference to it:
            Exception as e

This defines a pointer "e" that points to the object created above.

Probably the most important thing to realise about exception handling is that once an exception is raised, code
transfers directly to the exception handler; it is a "GOTO" technology.  All remaining statements in the try block
are skipped.  Thus only the first problem is detected, there could be other undetected problems in the try block
in the code that gets skipped.

In this example, we detect problems when "x" gets too large.  Also, the Python runtime will detect division by zero
for smaller values of "x".
'''

def main():
    """ try different values of x and y to trigger exceptions"""
    try:
        x = 10
        y = 0
        
        if x > 150:
            raise Exception("x is much too big")
        if x > 50:
            raise Exception("x is too big")
    
        print(f"x is {x}")
        print(f"x/y is {x/y}")  # division by zero error detected by Python runtime
    except Exception as e:
        print(e)


main()
