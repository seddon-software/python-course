##################################################
#
#   Advanced pattern matching ...
#
##################################################

import re

def test(name, pattern):
    text = "AAAA1111BBBB2222CCCC3333DDDD"
    print(pattern)
    compiledPattern = re.compile(pattern, re.X)
    matcher = compiledPattern.search(text)
    print((name + "<" + matcher.group(1) +
                  "><" + matcher.group(2) +
                  "><" + matcher.group(3) + ">" ))

test("Greedy:     ", r"^(.+)(\d+)(.+)$")
test("Non-Greedy: ", r"^(.+?)(\d+)(.+)$")

