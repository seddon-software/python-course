############################################################
#
#    sets
#
############################################################

# set up a list
sequence1 = 1, 3, 7, 5, 5, 4, 3, 2, 1
sequence2 = 2, 4, 6, 8, 6, 4, 3, 2, 1

# convert to set (duplicates are removed)
set1 = set(sequence1)
set2 = set(sequence2)

print(set1)
print(set2)

# mathematical operations on sets
unionSet = set1.union(set2)
intersectionSet = set1.intersection(set2)
differenceSet = set1.symmetric_difference(set2)

print(unionSet)
print(intersectionSet)
print(differenceSet)

1
