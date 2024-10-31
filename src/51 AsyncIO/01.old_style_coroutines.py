import os; os.system("clear")
'''
Coroutines were introduced as long ago as Python 2.5.  Coroutines were essentially generators that had additonal
capabilities: the yield statement could be used on the right hand side of an expression to allow data to be
fed to the geenerator (rather than the traditional yield which always 'generates' data).

Here is an example of these enhanced generators.  The main() function is such a generator; it takes in a number
and returns its square.

Note: when you call a generator function for the first time, the run-time creates an iterator and does not call
the function (as discussed in the section on generators).
'''

import asyncio
import time

# this is a coroutine (related to a generator)
def main():
    while(True):
        time.sleep(1)
        n = yield
        yield n**2

cr = main()              # calling main creates a coroutine, but doesn't run it
print(type(cr))

for n in range(10):
    next(cr)
    print(cr.send(n), end=", ")

