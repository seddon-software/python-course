'''
comprehensions
==============

The full set of comprehensions is:
    list comprehension
    dict comprehension
    set comprehension
    generator comprehension

with the following syntax
    list        [ fn(item) for item in sequence ]
    dict        { key:value for item in sequence }
    set         { fn(item) for item in sequence }
    generator   ( fn(item) for item in sequence )


Python comprehensions are a combination of map and filter.  The list comprehension is by far the most common.

The syntax is a little confusing:
            [ fn(item) for item in sequence ]
The [] mean the comprehension will create a list.  The items in the list are computed using
            fn(item)
where fn is some function and value takes on each value in the sequence.  Thus the comprehension is saying:
"create a list by applying fn to each item in the sequence".  In this form, the comprehension is equivalent
to the map() function.  As we will see below, a comprehension can also have a filter applied. 
'''

from math import sqrt

def cube(x):
    return x * x * x

# set up a sequence
sequence = list(range(1, 20))

# apply a comprehension to entire sequence
# for each x in sequence compute sqrt(x) and store the answers in a list
roots = [sqrt(x) for x in sequence]
print(roots)

# for each x in sequence compute x and store the answers in a list
n = [x for x in sequence if x < 10 ]      # identity transformation with filter applied
print(n)

# for each x in sequence compute cube(x) if x is even and store the answers in a list
cubes = [cube(x) for x in sequence if x%2==0 ]      # even number filter applied
print(cubes)

# other examples
print([ x + y for x in range(1,13) for y in range(1,13) if x*y > 120])
print([(x,y) for x in range(1,13) for y in range(1,13) if x*y > 120])    # create a list of tuples

# this is a 'prime' example of what not to do - far too complicated and difficult to understand
n = 1000 #some arbitrary stopping point
primes = [p for p in range(2, n)
           if p not in
            [np for i in range(2, int(n**0.5) + 1)  # i = 2,3,..31 
                for np in range(i * 2, n, i)]]  # np = 4,6,8 .. + 6,9,12 .. + 8,12,16 .. + 10,15,20 ..
print(primes)

# a much simpler way to generate primes
def isprime(num):
    return not [y for y in range(2,num) if num%y==0]

print([x for x in range(2,1000) if isprime(x)])

