'''
Strangely, although function objects are anonymous, the function object retains the name of its first reference
using the special attribute:
            __name__

If the function reference is changed we can still find the original name of the function from the exception
object! 
'''


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
