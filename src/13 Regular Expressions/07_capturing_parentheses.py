##################################################
#
#   Advanced pattern matching ...
#
##################################################

import re

string = "AAAA1111BBBB2222CCCC"

pattern = r"""^(           # capture-1
                (          # capture-2
                 (\D+)     # capture-3
                 (\d+)     # capture-4
                )
                (          # capture-5
                 (\D+)     # capture-6
                 (\d+)     # capture-7
                )
                 (\D+)     # capture-8
               )$"""
compiledPattern = re.compile(pattern, re.VERBOSE)
             
result = compiledPattern.search(string)

# print individual captures
print(result.group(1))
print(result.group(2))
print(result.group(3))

for i, group in enumerate(result.groups()):
    print(i+1, group)

1
