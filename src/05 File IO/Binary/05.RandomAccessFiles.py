'''
Random Access
=============

File IO is primarily designed to work with files sequentially.  However the "seek" method allows you to
jump around in the file.  This is useful if you know the detailed file format.

            myFile.seek(40, 0)

Jumps to byte 40 in the file; if the second parameter is:
            0   40 bytes from the start of the file
            1   40 bytes from the current position in the file
            2   40 bytes from the end of the file (offset is usually negative in this case)

The code below writes "ABCDEFGH" at byte 40 encodes as UTF-8 (default) and then again at byte 140 and 240.
The space between is filled with nulls by the O/S.  Finally, we jump to a very large byte position (2560240)
and write an X.

Note the file size will be determined by the last write, but the actual disk space used will be much less
because empty (4K) blocks are not allocated disk space.
'''

import os

fileName = 'data/myfile-5.bin'
try:
    with open(fileName, 'wb') as myFile:
        myFile.seek(40, 0)
        myFile.write("ABCDEFGH".encode())

        myFile.seek(140, 0)
        myFile.write("ABCDEFGH".encode())

        myFile.seek(240, 0)
        myFile.write("ABCDEFGH".encode())

        myFile.seek(2560240, 0)
        myFile.write("X".encode())
except Exception as e:
    print(e)

os.system(f"hexdump -cx {fileName}")
os.system(f"ls -l {fileName}")
