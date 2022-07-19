'''
Formatting Integers
===================

Python allows formatting numbers as
    b       = binary
    o       = octal
    x and X = hexadecimal
    d       = decimal

Decimal notation is also the default if nothing is specified.  The numeric prefix indicates the width of
the output in characters notmally padded by blanks, but as shown below it can be padded by zeros.

Larger numbers can be split into groups using either the comma or underscore separator.  Justification uses 
the > and < symbols.
'''

n = -7612
print(f"binary:  {n:20b}")
print(f"octal:   {n:20o}")
print(f"hex:     {n:20x}")
print(f"HEX:     {n:20X}")
print(f"decimal: {n:20d}")
print(f"default: {n:20}")
print(f"HEX:     {n:020X}")
print(f"right:   {n:>20}justification")
print(f"left:    {n:<20}justification")


n = 123456789
print(f"separator: <{n:_}>")
print(f"separator: <{n:,}>")
