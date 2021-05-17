# whitespace = ' \t\n\r\v\f'
# ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
# ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# ascii_letters = ascii_lowercase + ascii_uppercase
# digits = '0123456789'
# hexdigits = digits + 'abcdef' + 'ABCDEF'
# octdigits = '01234567'
# punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
# printable = digits + ascii_letters + punctuation + whitespace

# 'résumé'
s = "résumé".encode("utf-8")
print(type(s))
print(s)

b = b"r\xc3\xa9sum\xc3\xa9".decode("utf-8")
print(type(b))
print(b)

# 'El Niño'
s = "El Niño".encode("utf-8")
print(type(s))
print(s)

b = b"El Ni\xc3\xb1o".decode("utf-8")
print(type(b))
print(b)
