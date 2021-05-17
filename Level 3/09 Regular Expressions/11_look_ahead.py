#######################################################
#
#       lookahead
#
#######################################################

import re

# Search criteria:
# 1) filenames with an extention
# 2) extension must not be .bat

def test(pattern):
    splitPattern = re.compile(r";[ ]+")
    for key, value in  (iter(tests.items())):
        text, expected = splitPattern.split(value, 1)
        compiledPattern = re.compile(pattern, re.X)
        matcher = compiledPattern.search(text)
        if (matcher is not None and expected == "VALID"):
            print("PASS", end=' ')
        elif(matcher is None and expected == "INVALID"):
            print("PASS", end=' ')            
        else:
            print("FAIL", end=' ')
    print()


tests = {
          1 : "f1.txt;   VALID", 
          2 : "f2.;      INVALID", 
          3 : "f3.bat;   INVALID", 
          4 : "f4,pdf;   INVALID",
          9 : "f5..html; INVALID", 
          6 : "f6..;     INVALID",
          7 : "f7.chm;   VALID",
          8 : ".txt;     INVALID",
          9 : "f5.hbat;  VALID", 
        }

test(r".*[.].*$")
test(r".+[.].+$")
test(r"\w+[.]\w+$")
test(r"\w+[.](?!bat)\w+$") # should all pass






1