from timeit import timeit

# compare two ways of performing sqrt (1,000,000 iterations)
print("import {:0.6f}".format(timeit('math.sqrt(50.0)','import math')))
print("from   {:0.6f}".format(timeit('sqrt(50.0)','from math import sqrt')))

# just do 10,000 iterations
print("import {:0.6f}".format(timeit('math.sqrt(50.0)','import math', number=10*1000)))
print("from   {:0.6f}".format(timeit('sqrt(50.0)','from math import sqrt', number=10*1000)))

1
