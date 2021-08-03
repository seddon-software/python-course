import unicodedata

# create a string from unicode code points
u = chr(0x1F5A4) + chr(0x221B) + chr(0xF523)
print(type(u))
print(u)

# utf-8 uses a different encoding than raw code points
b = u.encode('utf-8')
print(b)

s = b.decode('utf-8')
print(s)
