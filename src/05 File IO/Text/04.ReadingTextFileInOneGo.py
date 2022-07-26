'''
Reading Text File In One Go
===========================

Text files don't have to be read a line at a time.  The file object ("f") has a method to read all lines of
the text file in a single call.  This returns a list with each line as a seperate entry in the list.
'''

def getFileContents(filename):
    try:
        with open(filename, "r") as f:
            allLines = f.readlines()
            print(type(allLines))
    except IOError as e:
        print(e)
    return allLines

lines = getFileContents("data/hello.txt")
for n,line in enumerate(lines):
    # add line numbers
    print(f"{n+1}: {line}", end="")
    
