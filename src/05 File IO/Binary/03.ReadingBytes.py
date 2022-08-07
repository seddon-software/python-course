'''
Reading a File of Bytes
=======================

Binary I/O (also called buffered I/O) expects bytes-like objects and produces bytes objects. No encoding, decoding, 
or newline translation is performed.
'''

fileName = "data/myfile-1.bin"

try:
    with open(fileName, "rb") as f:     # "b" is required even in Linux
        bytesObject = f.read()
        print(f"{type(bytesObject)} = {bytesObject}")
        # convert to integers 
        print(f"as a list = {list(bytesObject)}")
except IOError as e:
    print(e)
    