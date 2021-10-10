'''x and y end up different even though the same operations are applied to
both (supposedly identical) lists'''

x = [[0],[0]]
y = [[0]]*2
if x == y: print("same")
if not x is y: print("not identical")
x[0].append(7)
y[0].append(7)
print(x)
print(y)
print(f"ids of x: {id(x[0])}, {id(x[1])}")
print(f"ids of y: {id(y[0])}, {id(y[1])}")
