"""
Write a program that concatenates three files into a new file.
"""

inFile1 = inFile2 = inFile3 = outFile = None

try:
    inFile1 = open("data/TestFile1.txt", "r")
    inFile2 = open("data/TestFile2.txt", "r")
    inFile3 = open("data/TestFile3.txt", "r")
    outFile = open("data/TestFile.txt", "w")

    for file in (inFile1, inFile2, inFile3):
        for line in file:
            outFile.write(line)
except IOError as reason:
    print(reason)
finally:        
    if inFile1: inFile1.close()
    if inFile2: inFile2.close()
    if inFile3: inFile3.close()
    if outFile: outFile.close()


1