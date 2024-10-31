import os; os.system("clear")
'''
UTF-8 Encoding
==============
Here are some examples of the UTF-8 encoding and the bytes used to represent the encodings.  UTF-8 byte encodings
are between 1 and 4 bytes long, see:
            https://en.wikipedia.org/wiki/UTF-8
'''

# 'résumé'
s = "résumé".encode("utf-8")  # convert to bytes using UTF8 encoding
print(type(s))          # bytes
print(s)
print(s.hex())          # display as hex

# reverse the above
b = b"r\xc3\xa9sum\xc3\xa9".decode("utf-8") # decode a byte string assuming UTF8 encoding
print(type(b))          # str
print(b)

# alternatively reverse this way
b = bytes(bytearray(b'\x72\xc3\xa9\x73\x75\x6d\xc3\xa9'))
print(type(b))
print(b)
print(b.decode("utf-8"))    # str

# repeat with 'El Niño'
s = "El Niño".encode("utf-8")
print(type(s))              # bytes
print(s)
print(s.hex())

# reverse the above
b = b"El Ni\xc3\xb1o".decode("utf-8")
print(type(b))              # str
print(b)
