"""
Write a program that prints out the first 20 Fibonacci 
numbers.  You can use the web to find out the definition 
of the Fibonacci sequence.
"""
a, b = 0, 1

for n in range(20):
    print(f"{a}", end=" ") 
    a, b = b, a+b
    
