import profile

def fib(n):
    if n == 0: return 0
    if n == 1: return 1
    return fib(n-1) + fib(n-2)

def fibonacci_seq(n):
    seq = [ ]
    if n > 0:
        seq.extend(fibonacci_seq(n-1))
    seq.append(fib(n))
    return seq

profile.run('print(fibonacci_seq(20)); print()')

1
