'''
Writing to a Text File
======================
Similarly, you can write to a text file in one go.  However, you will obviously need to have all the text for the 
file in memory before writing.

Note when a file is opened in "w" (write) mode, the file is truncated (contents removed) prior to the first write.
'''

def writeFileContents(filename, data):
    try: 
        # w (write) will empty an existing file before opening it
        with open(filename, "w") as f:
            f.writelines(data)
    except IOError as e:
        print(e)

FILENAME = "data/text.txt"
data = ("line 1\n", "line 2\n", "line 3\n", "line 4\n", "line 5\n")
writeFileContents(FILENAME, data)

import os
os.system(f"cat {FILENAME}")


