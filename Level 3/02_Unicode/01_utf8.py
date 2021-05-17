s1 = "ABCDEF"
print(s1)

b1 = s1.encode('utf-8')
print(b1)

s2 = b1.decode('utf-8')
print(s2)

b2 = b"ABCDEF"
print(b2)

s3 = b2.decode('utf-8')
print(s3)

# use incorrect encoding
s3 = b2.decode('utf-16')
print(s3)


