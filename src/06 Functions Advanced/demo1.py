def square(n):
    return n**2

print(square(6))
f = square

square = 99
print(square)

print(f(6))
print(square(6))
