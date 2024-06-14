'''
Generators
==========

A generator that yields ints is secretly just a iterator that
returns ints
'''

############################################################
# 1) run the program
############################################################
from typing import Iterator

def gen(n: int) -> Iterator[int]:
    i = 0
    while i < n:
        yield i
        i += 1

g = gen(10)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print()

############################################################
# 2) perform static analysis with mypy
############################################################

import os
print(f"mypy {os.path.basename(__file__)}")
os.system(f"mypy {os.path.basename(__file__)}")
