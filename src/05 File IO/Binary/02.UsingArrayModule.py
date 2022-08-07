'''

Thd Array module defines an object type which can compactly represent an array of basic values: characters, 
integers, floating point numbers. Arrays are sequence types and behave very much like lists, except that the type 
of objects stored in them is constrained. The type is specified at object creation time by a single character code. 

In this example the array is of unsigned char (int) denoted by a 'B'.  Thus the line
            a = array.array('B', [65]*100)

creates an array with 100 unsigned chars with ascii code 65 ('A').  Then the array is extended by 100 bytes filled
with nulls (code 0).  Finally, the array is extended by a further 100 bytes filled with code 66 ('B').

The array is then dumped to a file and we use hexdump to look inside the file.
'''

import array
import subprocess

# open a binary file and add 300 bytes: [65]*100, [0]*100, [66]*100
try:
    fileName = "data/myfile-4.bin"
    with open(f"{fileName}", "wb") as f:
        a = array.array('B', [65]*100)
        a.extend([0] * 100)
        b = array.array('B', [66]*100)
        a.extend(b)
        a.tofile(f)
except IOError as e:
    print(e)
subprocess.run(f"hexdump -cx {fileName}".split())

