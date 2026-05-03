'''
Most superscripts and subscripts are in the range: 2070–209F
but were defined in ealier releases of Unicode and are in the range: 00B2-00B9

Greek and Coptic characters are in the range: 0370–03FF

Combining Diacritical Marks is a Unicode block (0300-036F) containing the most common combining characters
You can use unicodedata.normalize to combine characters
'''

# subscripts
print("E\u2095")  # Eₕ
print("F\u2096")  # Fₖ

# superscripts
print("A\u00B2")  # A²
print("B\u2077")  # B⁷

# greek letters
print("\u03B1\u03B2\u03B3\u03B4\u03B5\u03B6\u03B7\u03B8\u03B9\u03BA\n")   # αβγδεζηθικ

# combining characters
from unicodedata import normalize
char = 'a'
mark = '\u0302'  
print(normalize("NFC", char + mark))        # â
mark = '\u0305'  
print(normalize("NFC", char + mark))        # a̅
mark = '\u0324'  
print(normalize("NFC", char + mark))        # a̤
