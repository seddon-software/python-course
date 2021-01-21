############################################################
#
#    yield.py
#
############################################################



# iterate over a collection
myIterator = iter([11,22,33])   # iter() is a builtin that returns an iterator
for item in myIterator:
    print('item:', item)

# define your own iterator (using yield) that wraps the builtin iterator
def getIterator(collection):
     i = iter(collection)
     for item in i:
         yield '<%s>' % item
         print("debug")

myCollection = [111,222,333]
for x in getIterator(myCollection): 
    print(x)


# use a formula
def formula():
    x = 1
    y = 1
    while(y < 1000):
        yield y
        x = x + 1
        y = x * x

for n in formula():
    print(n)

1

