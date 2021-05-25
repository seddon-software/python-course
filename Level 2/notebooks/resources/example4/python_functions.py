def say_hello():
    print("say_hello from python")

def say_goodbye():
    print("say_goodbye from python")

def fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return a

def sumOfSquares(lo, hi):
    sum = 0.0
    for n in range(lo, hi + 1):
        sum += n**1.1
    return sum
