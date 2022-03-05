'''
This example modifies a string based on the complex delimiters:
              "\\s*([;:])\\s*"
 
The delimeter pattern is 0 or more spaces followd by a semi-colon or colon followed by 0 or more spaces.  The 
pattern also uses capture parentheses around the semi-colon or colon.  This enables us to use part of the original
delimiter in the replacement pattern:
              "--\1--"
The \1 is the first capture (the semi-colon or colon).  Thus we replace the complete delimiter with either
              --:-- or --;--
depending on whether we detected a semi-colon or a colon in the original delimeter.
'''

import re

# re.sub(pattern, repl, string, count=0, flags=0)

pattern = re.compile(r"\s*([;:])\s*")
string = "aaa  ; bbb :ccc     ;        ddd :  eee"
repl = r"--\1--"
newText = re.sub(pattern, repl, string)
print("<", string)
print(">", newText)

