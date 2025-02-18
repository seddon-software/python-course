#!/usr/bin/env python

import sys

class InvalidInput(Exception): pass

def process_input(a, b, operation):
    """Perform operation on a and b depending on the operation provided."""

    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b == 0: raise InvalidInput()
        return a / b

# if __name__ == "__main__":
#     "Run as a script"
#     # the following lines will be excluded from the coverage report
#     p1 = int(sys.argv[1])            # pragma: no cover
#     p2 = int(sys.argv[2])            # pragma: no cover
#     p3 = int(sys.argv[3])            # pragma: no cover
#     print(process_input(p1, p2, p3)) # pragma: no cover

