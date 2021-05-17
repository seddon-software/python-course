def powers():
    x = 1
    while(True):
        x = x * 2
        yield x

# create the infinite generator
g = powers()

x = 0
while x < 1000:
    x = next(g)
    print(x)
    
for n in range(10):
    print(next(g)) 
       
