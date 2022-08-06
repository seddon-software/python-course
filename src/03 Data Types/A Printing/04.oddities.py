'''
Printing Oddities
=================
Here are some examples of printing special characters in f-strings.  We can also justify strings as left, right 
or center with or without padding characters.

'''

# special characters
print(f"{{")
print(f"}}")
print(f"\\")

# justification
s = "ABCDEFGHIJKLM"
print(f"default: <{s:20}>")
print(f"left:    <{s:<20}>")
print(f"right:   <{s:>20}>")
print(f"center:  <{s:^20}>")
print(f"padding: <{s:?^20}>")
