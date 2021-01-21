"""
Write a function to calculate Factorials.  Try out
    factorial(1)
    factorial(10)
    factorial(40)
    factorial(100)
"""

def factorial(n):
    if n == 1: 
        return 1
    else:
        return n * factorial(n -1)

print(factorial(1))
print(factorial(10))
print(factorial(40))
print(factorial(100))

