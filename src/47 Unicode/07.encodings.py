'''
Encodings
=========
Unicode supports a number of different encodings.  In this example we compare encodings of the string "résumé".
Note that not all Unicode code points can be represented in some encodings and in particular, the Japanese encoding 
"shift_jis" can't represent "résumé".
'''

def encodeString(string, encoding):
    bytes = string.encode(encoding)
    print(f"{encoding}: {bytes}")

# see what set of bytes are produced using different encodings
encodeString("résumé", "utf-8")
encodeString("résumé", "utf-16")
encodeString("résumé", "utf-32")
encodeString("résumé", "Latin-1")
encodeString("résumé", "mac_roman")
encodeString("résumé", "mac_turkish")
try:
    encodeString("résumé", "shift_jis") # Japanese
except Exception as e:
    print(e)
