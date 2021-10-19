############################################################
#
#    random access
#
############################################################

myFile = open('data/myfile2.bin', 'wb')

myFile.seek(40, 0)
myFile.write("ABCDEFGH".encode())

myFile.seek(140, 0)
myFile.write("ABCDEFGH".encode())

myFile.seek(240, 0)
myFile.write("ABCDEFGH".encode())

myFile.seek(2560240, 0)
myFile.write("X".encode())

myFile.close()

import os
os.system("hexdump data/myfile2.bin")
