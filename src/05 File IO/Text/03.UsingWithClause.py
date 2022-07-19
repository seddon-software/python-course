'''
Using With Statements
=====================
The previous example can be simplified using a "with" statement.  A "with" statement gets expanded to a try-finally 
block by the Python compiler.  The example below is entirely equivalent to the previous example.

"with" statements are called context managers; prefer to use "with" statements rather than try-finally.
'''

# successful read
try:
    with open("data/hello.txt", "r") as f:
        for line in f:
            print(line, end="")
except IOError as e:
    print(e)

# unsuccessful read
try:
    with open("data/unknown-file.txt", "r") as f:
        for line in f:
            print(line, end="")
except IOError as e:
    print(e)


