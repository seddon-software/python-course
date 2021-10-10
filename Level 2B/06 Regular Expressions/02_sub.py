#######################################################
#
#       sub
#
#######################################################

import re

# re.sub(pattern, repl, string, count=0, flags=0)

pattern = re.compile(r"\s*([;:])\s*")
string = "aaa  ; bbb :ccc     ;        ddd :  eee"
repl = r"--\1--"
newText = re.sub(pattern, repl, string)
print("<", string)
print(">", newText)

1