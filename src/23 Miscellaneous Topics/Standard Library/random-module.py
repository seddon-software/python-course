import random

print("random numbers:")
print("range [0.0 to 1.0):", random.random())
print("range [1.0 to 8.0):", random.uniform(1, 8))
print("range [3 to 8]:", random.randint(3, 8))
print("range [10,12, .. 20]:", random.randrange(10, 21, 2))
print("range [a-z]:", random.choice('abcdefghijklmnopqrstuvwxyz'))