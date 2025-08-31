'''
slicing
=======

You can create sub-arrays of list and tuples using slices.  Slices are objects in themselves and can be passed to
functions, but are usually used directly to produce sub-arrays when applied to lists and tuples.  They are closely 
related to ranges and follow the same convention of parameters being defined as:
            slice(lower-bound, upper-bound, step)

Note that you can omit parts of a slice:
            colors[1:]        # upper bound is end of list
            colors[:-3]       # lower bound is start of list
            colors[:]         # default slice (creates a copy of the list)
'''

# slicing lists
colors = ["red", "blue", "green", "white", "black"] 
print(colors[2])        # the third item
print(colors[-1])       # counting backwards (the last item)
print(colors[1:3])      # items 1 and 2
print(colors[1:])       # items 1 to last
print(colors[-3:-1])    # items -3 and -2 
print(colors[4:1:-1])   # items 4, 3 and 2, working backwards
colors[2:4] = ("purple", "cyan") # change items 2 and 3
print(colors[0:])       # items 0 to end
print(colors[:])        # same
print(colors)           # same again

# using slice by passing it to a function
slice = slice(4,10,2)

def useSlice(s):
    print(type(slice))
    print(slice)
    array = list(range(20)) # create a test array
    print(array[s])         # slice it
    
useSlice(slice)
