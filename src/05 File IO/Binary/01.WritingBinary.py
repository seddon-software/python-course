'''
Writing Binary
==============

When writing binary data to a file, you have several altrnatives:
    1) use bytes
    2) use bytearray
    3) use struct

Using bytes is the most straightforward; simply set all the bytes up as a bytes string.  Note that the OS 
may perform bytes swapping.  Alternatively, you can set up your data in a list and then convert to a bytearray
as shown below.

Using struct is for more complex cases.  We show a simple example of a list of bytes, but for more information:
            https://docs.python.org/3/library/struct.html
'''

import os

def writeBinary(filename, data):
    try:
        with open(filename, "wb") as f:
            f.write(data)
    except IOError as e:
        print(e)


# use bytes
fileName = 'data/myfile-1.bin'
data = b"\x5F\x9D\x3E\x5F\x00\x00\x00\x00\x9D\x3E\x5F\x9D\x3E\x5F\x9D\x3E\x5F\x9D\x3E"
writeBinary(fileName, data)
os.system(f"hexdump {fileName}")
print()

# use a bytearray
fileName = 'data/myfile-2.bin'
data = bytearray([0x5F,0x9D,0x3E,0x5F,0x00,0x00,0x00,0x00,0x9D,0x3E,0x5F,0x9D,0x3E,0x5F,0x9D,0x3E,0x5F,0x9D,0x3E])
writeBinary(fileName, data)
os.system(f"hexdump {fileName}")
print()

# use struct
import struct
import binascii
import ctypes

print(f'struct format: {len(data)}s')
rawBuffer = struct.Struct(f'{len(data)}s')
stringBuffer = ctypes.create_string_buffer(rawBuffer.size)

print(('Before  :', binascii.hexlify(stringBuffer.raw)))
data = b"\x5F\x9D\x3E\x5F\x00\x00\x00\x00\x9D\x3E\x5F\x9D\x3E\x5F\x9D\x3E\x5F\x9D\x3E"
rawBuffer.pack_into(stringBuffer, 0, data)
print(('After  :', binascii.hexlify(stringBuffer.raw)))
writeBinary('data/myfile-3.bin', stringBuffer)



