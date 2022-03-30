'''
Consuming Generators
====================

Finite generators run out of data if you call next() enough times.  If that happens, the generator will raise
a StopIteration exception.  This exception can sometimes get hidden by builtin functions.  

In this example we use the sum() builtin.  sum() will exhaust the generator and handle the exception, but will
return the sum of all the generated values.  However, if you call sum() a second time, the generator will already
be exhausted and raise the exception immediately; sum() will return 0 in this case.
'''

roots = (x for x in range(10))   # identity generator

print(sum(roots))   # consume the generator
print(sum(roots))   # the generator is now empty







