def encodeString(string, encoding):
    bytes = string.encode(encoding)
    print(f"{encoding}: {bytes}")

# résumé
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
