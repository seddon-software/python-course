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
format = "%32.20g"
print(type(x))
print((format % x)) 

############################################################
# integers
x = 100
x += 1
print(type(x))
print(x)

x = 0o53
print(x)

x = 0xFF
print(x)

############################################################
# None
x = None   # => not defined
print(type(x))
print(x)

if (x == None):
    x = 240

print(x)

############################################################
# strings
x = 'hello'
y = "from"
z = '''the
planet
earth'''
print(x + y + z)
