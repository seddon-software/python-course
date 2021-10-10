############################################################
#
#    Data Types
#
############################################################

############################################################
# boolean
x = True
y = False

z = x or y
print(z)

z = x and y
print(z)
print(type(z))

############################################################
# complex
x = (+2.5-3.4j) - (-1.4+1.0j)
print(type(x))
print(x)

print(x.real)
print(x.imag)

############################################################
# floating point
x = 1e4 + 0.1e-4
print(type(x))
print(f"{x:32.20g}") 

############################################################
# integers
x = 100
x += 1
print(type(x))
print(x)

x = 0o53        # octal starts with 0o
print(x)

x = 0xFF        # hex starts with 0x
print(x)

############################################################
# None
x = None   # None means not defined
print(type(x))
print(x)

if (x == None):
    x = 240

print(x)

############################################################
# strings (use either quotes)
x = 'hello'
y = "from"
# triple quoted string (multi-line)
z = '''the
planet
earth'''
print(x + y + z)

# raw strings (\ not interpolated)
s = "abc\ndef"
print(s)        # \n is interpolated as a new line
r = r"abc\ndef" # \n is not interpolated
print(r)
