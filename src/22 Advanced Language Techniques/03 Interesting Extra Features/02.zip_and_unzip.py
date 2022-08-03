'''
zip and unzip
=============
The zip builtin is handy when you need to operate on several lists simultaneously.  You can zip several lists
together or reverse the process and unzip.  The zip function can also be used in comprehensions and to transpose
a matrix.
'''

# zip together 2 lists
A = [1, 2, 3, 4, 5]
B = ["a", "b", "c", "d", "e"]
AB = list(zip(A, B))
print(AB)

# zip 3 sequences
C = ("v", "w", "x", "y", "z")
ABC = list(zip(A, B, C))
print(ABC)

# using a comprehension
ABC = [(p1, p2, p3) for p1, p2, p3 in zip(A, B, C)]
print(ABC)

# unzip ABC
A, B, C = list(zip(*ABC))
print(A)
print(B)
print(C)

# you can transpose a matrix using zip
a = [[1,2,10], [3,4,20], [5,6,30]]
print((list(zip(*a))))

# you can wrap this up as a function
def transpose(x): 
    return list(zip(*x))

print((transpose(a)))