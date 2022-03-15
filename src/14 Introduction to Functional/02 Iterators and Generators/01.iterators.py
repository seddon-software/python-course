'''
Iterators
=========

Python iterators are defined as classes that support the following methods: __iter__() and __next__().
Amongst other things, Python provides special language support for iterators when used in a for loop.  We will 
be investigating this support below.

First we create a Fibonacci class with methods __iter__ and __next__.  Objects of this class will be iterators.
The special language support in loops means that
                for f in Fibonacci():
                    print(f, end=", ")

is expanded by the run-time into
    try:
        fib = Fibonacci()
        iter = fib.__iter__()

        f = iter.__next__()
        print(f, end=", ")

        f = iter.__next__()
        print(f, end=", ")

        f = iter.__next__()
        print(f, end=", ")

        # and so on until an exception is raised when the iterator is exhausted
    except StopIteration as e:
        pass

Once the iterator is created with
        fib = Fibonacci()
the __iter__() method is called once on "fib".  The return from this method designates the iterator object used 
in the remainder of the loop.  Often that will be the "fib" object that was created above, but it could be another
iterator object if you want.  If you want to use "fib" then simply return self from __iter__().

After "f" is returned from f.__iter__(), the loop calls f.__next__() until the iterator is exhausted, when it will
raise a "StopIteration" exception.  The run-time will then catch the exception and terminate the loop.
'''

############################################################
#
#    iterators
#
############################################################

# iterators must support two methods: 
 
class Fibonacci:
    def __init__(self):
        self.x,self.y = 0,1
        
    def __iter__(self):
        return self  # the object on which to call next() - usually ourself

    def __next__(self):
        if self.x > 100:
            raise StopIteration     # indicate end of iteration
        
        self.x, self.y = self.y, self.x + self.y
        return self.x

    
# create an instance of class and invoke iterator methods
# __iter__(self) will be called once
# __next__(self) will be called repeatedly until loop terminates


for f in Fibonacci():
    print(f, end=", ")


# The above loop gets translated to:
#
# try:
#     fib = Fibonacci()
#     iter = fib.__iter__()

#     f = iter.__next__()
#     print(f, end=", ")

#     f = iter.__next__()
#     print(f, end=", ")

#     f = iter.__next__()
#     print(f, end=", ")

#     f = iter.__next__()
#     print(f, end=", ")

#     f = iter.__next__()
#     print(f, end=", ")

#     f = iter.__next__()
#     print(f, end=", ")

#     f = iter.__next__()
#     print(f, end=", ")

#     f = iter.__next__()
#     print(f, end=", ")

#     f = iter.__next__()
#     print(f, end=", ")

#     f = iter.__next__()
#     print(f, end=", ")

#     f = iter.__next__()
#     print(f, end=", ")

#     f = iter.__next__()
#     print(f, end=", ")

#     f = iter.__next__()
#     print(f, end=", ")

#     f = iter.__next__()
#     print(f, end=", ")
# except StopIteration as e:
#     pass








