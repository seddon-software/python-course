"""
Try the previous example with other test files that may contain 
non integral data.  Use exception handling to filter out lines 
that don't contain integers.
"""

inFile = None
total = 0

try:
    inFile = open("data/TestData2.txt", "r")

    for line in inFile:
        try:
            total += int(line)
        except Exception as e:
            print(e)
except IOError as reason:
    print(reason)
finally:        
    if inFile: inFile.close()

print(f"Total = {total}")


1