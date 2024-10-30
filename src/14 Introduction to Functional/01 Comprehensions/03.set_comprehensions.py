import os; os.system("clear")
'''
Set Comprehension
=================

A set comprehension generates a set from a sequence.  It uses {} like a dict comprehension, but note the
absence of a : in the {}.  In this example, we use a sequence formed from two sequences; all x in range(10)
and all y in range(10).  Thus the final sequence will be 00, 01, 02 ... 10 11 12 ... 97 98 99.

Note that sets have all duplicates removed, so this set will be all possible sums of numbers from both ranges. 

'''
s = { x + y for x in range(10) for y in range(10) }     # 0, 1, 2 ... 18
print(s)

