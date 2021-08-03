#######################################################
#
#       split
#
#######################################################

import re

x = "hello-to-you".split("-")
print(x)

pattern = re.compile(r"[\s^;]+")
text = "  aaa  ; bbb ;ccc     ;    ^    ddd ;  eee   "
mylist = pattern.split(text.strip())
print(mylist)

