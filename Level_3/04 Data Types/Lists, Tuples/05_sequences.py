############################################################
#
#    sequences
#
############################################################

# set up sequences
sequence1 = 2, 3, 5, 7, 11, 13, 17
sequence2 = 'A', 'B', 'C', 'D', 'E', 'F', 'G'
sequence3 = 66, 24, 17, 25, 51, 98, 78
print(type(sequence1))

# iterate through sequence
for index, value in enumerate(sequence1):
    print(index, value, end=' ... ')
print()

# iterate through two sequences at once
for value1, value2 in zip(sequence1, sequence2):
    print(value1, value2, end=' ... ')
print()

# iterate in reverse
for value in reversed(sequence3):
    print(value, end=' ... ')
print()

# iterate in sorted sequence
for value in sorted(sequence3):
    print(value, end=' ... ')
print()


1
