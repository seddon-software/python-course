import os; os.system("clear")
'''
Unicode Strings
===============
Python3 uses Unicode for all strings.  If you want a Unicode string, but don't have an appropriate keyboard
to hand, you can build a string from Unicode code points as shown below:
'''

import unicodedata

# create a string from unicode code points
u = chr(0x1F5A4) + chr(0x221B) + chr(0x2230)  # black heart, cube root and triple integral
print(u)

