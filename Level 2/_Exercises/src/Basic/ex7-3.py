"""
Create a file call TestData.txt with test data consisting of one 
number per line using your favourite editor.  Your job is to read 
the entire file into memory so that you can compute the sum of all 
the numbers.
"""

inFile = None
total = 0

try:
    inFile = open("data/TestData.txt", "r")

    for line in inFile:
        total += int(line)
except IOError as reason:
    print(reason)
finally:        
    if inFile: inFile.close()

print(f"Total = {total}")

1