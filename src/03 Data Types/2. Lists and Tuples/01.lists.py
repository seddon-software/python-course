'''
list (mutable)
==============
Lists are mutable arrays.  Index starts at 0 and define and access with []. 
'''

# define several lists
x1 = []
x2 = [1]
x3 = [1,2,3,4,5]
x4 = [1, "mixed", 2, 'list']
x5 = [[1,2],[3,4]]

# print lists
print(f"type of x1: {type(x1)}")
print(f"{x1} has length {len(x1)}")
print(f"{x2} has length {len(x2)}")
print(f"{x3} has length {len(x3)}")
print(f"{x4} has length {len(x4)}")
print(f"{x5} has length {len(x5)}")

# access elements
print(f"element 0 of x3 is {x3[0]}")
print(f"element 1 of x3 is {x3[1]}")
print(f"element 2 of x3 is {x3[2]}")

# negative indices
print(f"last element of x3 is {x3[-1]}")
print(f"last but one element of x3 is {x3[-2]}")
print(f"last but two element of x3 is {x3[-3]}")

