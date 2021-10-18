x = 100             # x is a pointer to the integer 100
print(x, type(x), id(x))
x = 6.34            # x moves to point at float 6.34
print(x, type(x), id(x))
x = "ABC"           # x moves again
print(x, type(x), id(x))

# everything is either an object OR a pointer (object reference)
