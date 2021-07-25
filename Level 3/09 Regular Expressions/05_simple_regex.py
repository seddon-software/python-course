############################################################
#
#    Regular Expressions
#
############################################################


import re

text1 = "This line contains the number 8.73 and 4.67"
text2 = "This line does not contains any numbers"

numberPattern = r"\d+[.]\d+"
pattern = re.compile(numberPattern)
matcher1 = pattern.search(text1)
matcher2 = pattern.search(text2)

print(matcher1.group())
if matcher1:
    print("Pattern found in text1")
else:
    print("Pattern NOT found in text1")

if matcher2:
    print("Pattern found in text2")
else:
    print("Pattern NOT found in text2")
