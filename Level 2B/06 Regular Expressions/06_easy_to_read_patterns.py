##################################################
#
#   Advanced pattern matching ...
#
##################################################

import re

string = "AAAA1111BBBB2222CCCC3333DDDD";
pattern = r"""         
             ^        # start of line
             (.*?)    # 0 or more characters
                      # non greedy
             (\d+)    # 1 or more digits
             (.*)     # 0 or more characters
             $        # end of line
           """
           
compiledPattern = re.compile(pattern, re.VERBOSE)
result = compiledPattern.search(string)

print("Part1: ", result.group(1))
print("Part2: ", result.group(2))
print("Part3: ", result.group(3))


1;
