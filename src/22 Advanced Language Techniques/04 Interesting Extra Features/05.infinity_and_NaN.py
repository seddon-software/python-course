'''
Infinity and NaN
================
Python lets you work with 2 special floating point numbers
            inf         infinity
            NaN         not a number

This example shows what happens when you perform arithetic on these values.
'''

print(f"inf - 5000.0 = {float('infinity') - 5000.0}")
print(f"inf - inf = {float('infinity') - float('infinity')}")
print(f"inf + inf = {float('infinity') + float('infinity')}")
print(f"inf / inf = {float('infinity') / float('infinity')}")
print(f"inf * inf = {float('infinity') * float('infinity')}")
print(f"inf * 0.0 = {float('infinity') * 0.0}")
print(f"nan + 5.0 = {float('NaN') + 5.0}")
