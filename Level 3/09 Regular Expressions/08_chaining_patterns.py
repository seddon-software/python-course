##################################################
#
#   Advanced pattern matching ...
#
##################################################

import re

text = "AB12CD34EF56GH"
pattern = r"(\d+)"

# find all occurances of pattern
matcher = re.findall(pattern, text)
print(matcher)

# iterate through finding the pattern
for matcher in re.finditer(pattern, text):
    print(matcher.groups(0))



