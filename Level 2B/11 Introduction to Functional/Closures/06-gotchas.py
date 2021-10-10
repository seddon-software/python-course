# Closures close over variables, not values

############################################################
# Part 1 - closure gives 'unexpected' results
funcs = []
for i in range(4):
    def f():
        print(i)    # this closes over the (single) variable i
    funcs.append(f)

for f in funcs:
    f()             # i is now 3, so it prints 3 each time

print()

############################################################
# Part 2 - create extra instances of i for the closure
funcs = []
for i in range(4):
    def f(i=i):     # new i with local scope
        print(i)    # each i takes on a different value
    funcs.append(f)
    
for f in funcs:
    f()             # prints 0, 1, 2, 3

