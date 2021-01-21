"""
Write a function that takes a string and capitalises the first character of the string and ensures the remaining characters are converted to lower case.  Use the following test data:
    UpperFirst("test1")
    UpperFirst("mIxEdCaSe")
    UpperFirst("UPPER")
    UpperFirst("lower")
    UpperFirst("oPPOSITE")
"""

def UpperFirst(s):
    return s.capitalize()

print( UpperFirst("test1") )
print( UpperFirst("mIxEdCaSe") )
print( UpperFirst("UPPER") )
print( UpperFirst("lower") )
print( UpperFirst("oPPOSITE") )
