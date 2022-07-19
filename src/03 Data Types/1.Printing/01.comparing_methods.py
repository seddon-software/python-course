'''
Different Methods of Printing
=============================

Printing in Python has changed a lot over the years.  Originally influenced by the C language, Python 2 used the 
rather awkward % notation (and print statements omoitted the (); not permitted in Python 3).  In Python 3 it was 
decided to switch to the C# language method using {}.  This has been further improved by the introduction of 
f-strings.  f-strings should now be preferred on account of their simplicity.
'''

# define some variables for printing
s1 = "hello"
s2 = 'world'
x = 100
y = 200

# old Python 2 way of printing
print('Python 2 way of printing using %%: %s %s %i' % (s1, s2, x + y))

# Python 3 way
print('Python3 using format: {} {} {}'.format(s1, s2, x + y))
print('Python3 using format and numeric fields: {0} {1} {2}'.format(s1, s2, x + y))
print('Python3 using format and named fields: {x} {y} {z}'.format(x='hello', y='world', z = x + y))

# f strings
print(f'Python3 using f-strings: {s1} {s2} {x + y}')
