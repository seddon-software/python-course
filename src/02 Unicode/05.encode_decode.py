'''
Encode Decode
=============
Normally strings are represented by an encoding rather than code point values.  The idea behind encoding is to
efficiently store characters that are most likely to be used.  So for English speaking countries we use encodings
that favour the Latin character set; for Chinese speakers a different encoding would be more approriate.

There are many different encodings, but UTF-8 has become very popular on the web as it works reasonably efficiently 
for most common languages.  It is also the default encoding in Python (the one used if the encoding is not 
explicitly stated).

UTF-8 favours efficiency for English letters and other ASCII characters (one byte per character) while UTF-16 
favours several Asian character sets (2 bytes instead of 3 in UTF-8). This is what made UTF-8 the favorite choice 
in the Web world, where English HTML/XML tags are intermixed with any-language text. Cyrillic, Hebrew and several 
other popular Unicode blocks are 2 bytes both in UTF-16 and UTF-8.

When you want to pass a string across a network it has to be converted to bytes.  The "encode()" method is used 
for this purpose and "decode()" to reverse the encoding when the data arrives at its destination.  This leads
to the possiblity of a mix up with the encoding and a garbled result.
'''

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


