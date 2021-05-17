import collections

# Counter is a dict subclass for counting hashable objects (2.7 only)

# in this example the test data 'supercalifragilisticexpialidocious' is hashed
# each character is the key
# the number of occurances becomes the value
# and hence the result is a character count of the input string
myCounts = collections.Counter('supercalifragilisticexpialidocious')

print(myCounts);


1
