"""
Write a program that calculates the ratio of successive 
pairs of the first 200 Fibonacci numbers.  Does the ratio 
converge to a number?
"""

a, b = 0, 1

for n in range(200):
    print(a/b) 
    a, b = b, a+b
    
