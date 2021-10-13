s1 = "ABCDEF"       # UTF8 (default) string
print(s1)

b1 = s1.encode('utf-8') # convert to bytes
print(b1)

s2 = b1.decode('utf-8') # convert back to UTF8 string
print(s2)

b2 = b"ABCDEF"      # byte string (UTF8 by default)
print(b2)

s3 = b2.decode('utf-8') # decode to string
print(s3)

s3 = b2.decode('utf-16') # using incorrect encoding
print(s3)


