x = 100     # x points at 100
y = x       # y points at the same place as x, i.e. at 100

x += 1      # add one.  This points at a brand new integer
# all integers are IMMUTABLE

print(x, id(x))
print(y, id(y))
print(id(100))
print(id(101))
print(id(102))
print(id(103))

