from timings import Timings

def listComprehension(n):
    sum = 0
    X = [n*n for n in range(n)]
    for x in X:
        sum += x

def generatorExpression(n):
    sum = 0
    Y = (n*n for n in range(n))
    for y in Y: 
        sum += y
    
t1 = Timings(title = "lists",      setup = "from __main__ import listComprehension", 
                                   statement = "listComprehension(100000000)")

t2 = Timings(title = "generators", setup = "from __main__ import generatorExpression", 
                                   statement = "generatorExpression(100000000)")

Timings.titles()
t1.run(1)
t2.run(1)

