#!/usr/bin/env python

import sys

def process_input(a, b, operation):
    """Perform operation on a and b depending on the operation provided."""

    if operation == "add":
        return a + b
    if operation == "subtract":
        return a - b
    if operation == "multiply":
        return a * b
    if operation == "divide":
        if b == 0:
            return "Invalid Input"
        return a / b

if __name__ == "__main__":
    "Run as a script"
    print(process_input(int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]))

