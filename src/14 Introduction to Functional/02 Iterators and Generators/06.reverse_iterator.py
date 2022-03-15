'''
Reverse Iterator
================

You can easily built a reverse iterator using the reverse() and iter() functions.
'''

def reverse_iter(a):
    a.reverse()
    return(iter(a))

array = [2, 3, 4, 5, 6, 7, 8]
reverseIterator = reverse_iter(array)

for n in reverseIterator:
    print(n, end=", ")
print()
