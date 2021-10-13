s1 = 'hello'
s2 = 'world'

# old Python 2 way of printing
print('''Python 2 way of printing using %%: %s %s''' % (s1, s2))

# Python 3 way
print('Python3 using format: {} {}'.format(s1, s2))
print('Python3 using format and numeric fields: {0} {1}'.format(s1, s2))
print('Python3 using format and named fields: {x} {y}'.format(x='hello', y='world'))

# f strings
print(f'Python3 using f-strings: {s1} {s2}')
