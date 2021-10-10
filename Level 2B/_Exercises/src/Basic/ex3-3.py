"""
Use the range function to generate two separate tuples containing 
the list of integers from 10 to 19 and from 30 to 39.  
Tuples are immutable, so how can you form a tuple that has 
all the elements of the other two tuples
"""

tuple1 = tuple(range(10, 20))
tuple2 = tuple(range(30, 40))
theList = list(tuple1)

for i in range(10):
    theList.append(tuple2[i])
    
tuple3 = tuple(theList)
print(tuple3)     
