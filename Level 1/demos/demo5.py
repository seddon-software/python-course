import sys
sys.set_int_max_str_digits(2000000)

x = 1

for n in range(1, 100000):           # really 1 to 4
    x = x * n

print(x)
