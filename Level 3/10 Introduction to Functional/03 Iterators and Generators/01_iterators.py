############################################################
#
#    iterators
#
############################################################

# There is special language support for iterator in the for of a loop
# iterators must support two methods: __iter__ and __next__
 
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








