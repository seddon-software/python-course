'''
with statement
==============
The try finally block is used to implement the RAII pattern as discussed above.  However in practice
it is easier to use the "with" statement.  The "with" statement is functionally equivalent to the
try finally block.

This example shows how to open, read and subsequently close a file using both techniques.
'''

file = open("example.txt", "r")
try:
    content = file.read()
    print(content)
finally:
    file.close()  # Ensures the file is closed

with open("example.txt", "r") as file:
    content = file.read()
    print(content)  # File closes automatically