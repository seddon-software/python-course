'''
One final example.  We can use attribute lookup on a Point object, or cache values locally.  The later approach should be faster, but is 
only useful if the Point object is immutable
'''

from timeit import timeit

count = 1000 * 1000

t = timeit('distance = p.x * p.y', 'from myprogram import Point; p = Point(15, 33)', number = count)
print(f"attribute lookup {t:0.3f}")

t = timeit('distance = x * y',
           'from myprogram import Point; p = Point(15, 33); x = p.x; y = p.y',
            number = count)
print(f"using locals     {t:0.3f}")


1
