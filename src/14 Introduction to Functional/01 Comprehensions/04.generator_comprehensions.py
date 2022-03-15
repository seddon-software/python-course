'''
Generator Comprehensions
========================

The last comprehension to illustrate is generator comprehensions.  The syntax is almost identical to list
comprehensions, except the [] are replaced by ().  The use of () is unusual because () are often optional in 
arithmetic expressions; this is definately not the case with generator comprehensions, where () are MANDATORY.

Generator comprehensions employ lazy evaluations.  When such a comprehension is first created no code gets 
executed.  Its not until you call next() that code get executed.  This is similar to how lambdas work (also lazy 
evaluation).

One advantage of lazy evaluation is that it opens up the possibility of an infinite length comprehension.  Recall
that code only gets executed when next() is called.  With an infinite length comprehension you can continue to
call next() as long as you like.  Such comprehension will never get exhausted.

This demo compares list and generator comprehensions.  Step through the code an note how long each operation
takes.  Note the list comprehension of lambda functions also behaves in a lazy way.
'''

import time
print("start") 

# this takes 10 seconds to evaluate - each expression is evaluated
print((["no sleep", time.sleep(5), time.sleep(5)][0]))
print("list DONE")

# list comprehensions are evaluated immediately - takes 10 seconds
myComprehension = [time.sleep(n) for n in [0, 5, 5]]
myComprehension[0]
print("list comprehension DONE")
 
# generator comprehensions are evaluated in a lazy way
myIterator = (time.sleep(n) for n in [0, 5, 5])
next(myIterator)
next(myIterator)
print("generator comprehension DONE")


# lambdas are not evaluated until called - lazy evaluation
myLambdas = [lambda: time.sleep(5), lambda: time.sleep(5), lambda: "no sleep"]
myLambdas[2]()
print("lambdas DONE")



