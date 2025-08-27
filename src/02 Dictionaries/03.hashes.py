'''
A dictionary is sometimes called a hash map because it uses hashes to store its data.
Python has a built in function to compute hashes as illustrated below.

We normally hash strings, but can hash other immutable objects.  Note that two lexically similar strings
will hash to totally different numbers.
'''

# hash some similar strings (display in hex)
h1 = hash("Tom")
h2 = hash("Tim")
h3 = hash("Tam")
print(h1)
print(h2)
print(h3)

# guaranteed to be the same hash during the same run
print(h1)
print(h2)
print(h3)

# often used with remainder operator (%)
print(h1 % 100)
print(h2 % 100)
print(h3 % 100)

# hash a tuple
mytuple = (2, 4, 6, 8)
print(hash(mytuple))

# you can't hash mutable objects
mylist = [2, 4, 6, 8]
try:
    print(hash(mylist))
except Exception as e:
    print(e)


