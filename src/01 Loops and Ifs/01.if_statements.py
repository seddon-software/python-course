'''
Conditional Statements
======================

Examples of if statements (aka conditional statements) are shown below.  Note that indentatation is mandatory
for the bodies of if statements.  The indentation is usually 4 spaces, but can be any number as long as all
lines in the body use the same indentation.  You can also use any number of tabs (not recommended because of 
problems with hard copies).
'''

x = 10
a = 50
b = 100

if x > a:               # note colon
    print("x is > ", a) # note indentation (4 spaces)

if x > a:                   
    print("x is > ", a) # indentation must be the same for all statements in body
    print("x is > ", a)
    print("x is > ", a)

if x > a:              
    print("x is > ", a)
    print("x is > ", a)
    print("x is > ", a)
else:                   # can have an else branch
    print("x is <= ", a)
    print("x is <= ", a)
    print("x is <= ", a)

if x > b:              
    print("x is > ", b)
elif x > a:             # can have an elif branch (note order of comparisons)
    print("x is > ", a)
else:
    print("x is <= ", a)

