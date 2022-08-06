'''
sets
====

Sets support mathematical set operations:
    union                   combine sets
    intersection            common elements between sets
    symmetric difference    elements not appearing in both sets
'''

# set up a tuple
sequence1 = 1, 3, 7, 5, 5, 4, 3, 2, 1
sequence2 = 2, 4, 6, 8, 6, 4, 3, 2, 1

# convert to set (duplicates are removed)
set1 = set(sequence1)
set2 = set(sequence2)

print(f"set1: {set1}")
print(f"set2: {set2}")

# mathematical operations on sets
unionSet = set1.union(set2)
print(f"union: {unionSet}")

intersectionSet = set1.intersection(set2)
print(f"intersection: {intersectionSet}")

differenceSet = set1.symmetric_difference(set2)
print(f"difference: {differenceSet}")


