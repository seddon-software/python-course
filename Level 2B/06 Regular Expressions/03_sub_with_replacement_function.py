#######################################################
#
#       sub
#
#######################################################

import re

def f(matchObject):
    return f.pre + matchObject.group(1) + f.post

# re.sub(pattern, repl, string, count=0, flags=0)

pattern = re.compile(r"\s*([;:])\s*")
string = "aaa  ; bbb :ccc     ;        ddd :  eee"
f.pre = "--"
f.post = "++"
repl = f
newText = re.sub(pattern, repl, string)
print("<", string)
print(">", newText)

1