##################################################
#
#   Advanced pattern matching ...
#
##################################################

import re

test = "-------ABC------------"
pattern = r"\w+"
pattern = re.compile(pattern)

match = pattern.match(test)
print(match)

match = pattern.search(test)
print(match.group())

1


