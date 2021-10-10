#######################################################
#
#       translate
#
#######################################################

import re

days = { 'mon' : 'Monday', 
         'tue' : 'Tuesday',
         'wed' : 'Wednesday', 
         'thu' : 'Thursday', 
         'fri' : 'Friday' }

pattern = "(" + "|".join(list(days.keys())) + ")"
compiledPattern = re.compile(pattern)
print("pattern: ", pattern)

text = '''The course starts on mon, continues on tue,
          but thu is the last day'''

def replaceGroup(matcher):
    key = matcher.group(1)
    print(key)
    return days[key]

for matcher in re.finditer(compiledPattern, text):
    text = compiledPattern.sub(replaceGroup, text, 1)

print(text)

1
