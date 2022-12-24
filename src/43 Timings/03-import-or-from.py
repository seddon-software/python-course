'''
Using from is supposed to be slightly quicker than using import.  Let's use timeit to check things out.
'''

from timeit import timeit

def runit(title, stmt, setup, count):
    t = timeit(f'{stmt}', f'{setup}', number=count)
    print(f"count={count:<6}: {title} {t/count:0.10f}")

for count in 10000, 1000000:
    runit("import", "math.sqrt(50.0)", "import math", count)
    runit("from", "sqrt(50.0)", "from math import sqrt", count)

