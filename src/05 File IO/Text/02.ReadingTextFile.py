'''
Reading a Text File
===================
Use open to prepare a text file to be read into memory.  The open function returns a File object that knows how 
to read successive lines from the text file.  When f is used in a loop as in:
            for line in f:

line is set to successive lines of the file; each file has a file position indicator pointing at the current
position in the file.  The file position indicator is automatically incremented to the next line each time 
round the loop.

Its best to use exception handling when working with files (exception handling is covered in detail later in the 
course) because trying to open a file may fail for a number of reasons (no read acces, wrong name, wrong folder 
etc.).  The finally clause is guaranteed to be called even if an exception is thrown; this ensures the file is 
always closed properly.

The try-finally block can be simplified by using a "with" statement (see next example).
'''

# successful read
try: 
    f = open("data/hello.txt", "r")
    try:
        for line in f:
            print(line, end="")
    finally:
        f.close()
except IOError as e:
    print(e)


# unsuccessful read
try: 
    f = open("./data/unknown-file.txt", "r")
    try:
        for line in f:
            print(line, end="")
    finally:
        f.close()
except IOError as e:
    print(e)

