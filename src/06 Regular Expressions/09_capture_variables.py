##########################################################
#
#        Capture Variables
#
##########################################################

import re

testString = "---11112222333333334444555563366633777733---"
testPattern = "2+(3+)4+(5+)6+"

# search for pattern
pattern = re.compile(testPattern)
result = pattern.search(testString)
# print results
print("full match: ", result.group(0))
print("capture pattern 1: ", result.group(1))
print("capture pattern 2: ", result.group(2))
print("all captures: ", result.groups())
print(result.group())


1