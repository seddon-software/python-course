############################################################
#
#    function names
#
############################################################


# this function prints its original name, even if the function 
# reference is changed (see below)
def f():
    try:
        print(f"original function name is: {f.__name__}")
    except NameError as e:
        name = e.__str__().split()[1].strip("'")
        print(f"original function name is: {name}")


f()

# change the object reference
g = f
del f       # reference f is now invalid

# now call the function through the new reference
g()
