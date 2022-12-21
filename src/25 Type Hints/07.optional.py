'''
Optional
========
Optional is used for parameters that have default values.  In this example the "order" parameter of "orderInts()"
defaults to "ascending"; i.e. an optional parameter.

Optional[str] is a shorthand notation for Union[str, None], telling the type checker that either a str or None is
required.

This time we have a valid program.
'''

############################################################
# 1) run the program
############################################################
from typing import Optional

def orderInts(a:int, b:int, order:Optional[str]="ascending", **kwargs):
    lowest = a if a < b else b
    highest = a if a > b else b
    if not order or order=="ascending":
        print(f"order is {lowest}, {highest}")
    else:
        print(f"order is {highest}, {lowest}")

orderInts(6, 7, None)
orderInts(6, 7, "ascending")
orderInts(6, 7, "descending")
orderInts(6, 7)           # omit optional parameter

############################################################
# 2) perform static analysis with mypy
############################################################

import os
print(f"mypy {os.path.basename(__file__)}")
os.system(f"mypy {os.path.basename(__file__)}")
