# Python Weekly 474

s1 = 'hello'
s2 = 'world'

# old Python 2 way of printing
print('using %%: %s %s' % (s1, s2))

# Python 3 way
print('using format: {0} {1}'.format(s1, s2))
print('using format: {} {}'.format(s1, s2))

# f strings
print(f'f-strings: {s1} {s2}')
