"""
Write a file copy program
"""

inFile = None
outFile = None

try:
    inFile = open("data/original.txt", "r")
    outFile = open("data/copy.txt", "w")

    for line in inFile:
        outFile.write(line)
except IOError as reason:
    print(reason)
finally:        
    if inFile: inFile.close()
    if outFile: outFile.close()

1