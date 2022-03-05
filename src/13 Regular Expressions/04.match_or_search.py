'''
When we work with regular expressions we can "match"or "search".  The difference is that:
      matches have to match the entire string
      searches match on substrings
 
Note that in this example we are looking for the pattern "ABC" which is a substring of s.  Therefore the matcher 
will fail to find any matches (works with the whole string, not substrings), but the searcher will succeed.
 
The RegEx used has one set of capture parentheses; searcher returns 1 result - the first parenthesized match.
'''
import re

test = "-------ABC------------"
pattern = r"\w+"
pattern = re.compile(pattern)

matcher = pattern.match(test)
print(matcher)

searcher = pattern.search(test)
print(searcher.group())




