'''
Split
=====

This time we split a comma separated string of words into a list using a regex.
 
As a further example, we show how to split a string with a complex delimeter: the delimeter can
be any combination of spaces, semi-colons or hat symbols as defined by the RegEx:
                  [\\s^;]+
'''

import re

words = "hello-to-you".split("-")
print(words)

pattern = re.compile(r"[\s^;]+")
text = "  aaa  ; bbb ;ccc     ;    ^    ddd ;  eee   "
mylist = pattern.split(text.strip())
print(mylist)

