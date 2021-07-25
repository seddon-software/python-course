# timeit.timeit(stmt='pass', 
#               setup='pass', 
#               timer=<default timer>, 
#               number=1000000)

from timeit import timeit

count = 1000 * 1000

print("attribute lookup", timeit('distance = p.x * p.y', 
                                 'from myprogram import Point; p = Point(15, 33)',
                                 number = count))

print("using locals    ", timeit('distance = x * y',
                                 'from myprogram import Point; p = Point(15, 33); x = p.x; y = p.y',
                                 number = count))


1
