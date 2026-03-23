'''
sequences
=========

Sequences look like they are a new Python data type, but this is an illusion.  A comma separated list of items
is actually a tuple.  The Python compiler adds the () silently.

Sequences (or tuples) are also iteratators (see later in course) and as such can be used in loops.  The same is
true for lists.  Range objects are automatically cast to a tuple in loops.

zip can be used to combine the sequences.
'''

# set up sequences
sequence1 = 2, 3, 5, 7, 11, 13, 17
print(type(sequence1))
sequence2 = 'A', 'B', 'C', 'D', 'E', 'F', 'G'
sequence3 = 66, 24, 17, 25, 51, 98, 78

# iterate through sequence
for value in sequence1:
    print(value, end=', ')
print()     # blank line

# use enumerate to also determine the loop count (position in loop)
for i, value in enumerate(sequence1):
    print(i, value, end=' ... ')
print()

# iterate through three sequences at once
for value1, value2, value3 in zip(sequence1, sequence2, sequence3):
    print(value1, value2, value3, end=' ... ')
print()

# iterate in reverse
for value in reversed(sequence3):
    print(value, end=', ')
print()

# iterate in sorted sequence
for value in sorted(sequence3):
    print(value, end=', ')
print()

# using range in a loop
for x in range(1, 5):
    print(f"{x}, ", end="")
print()

