import os; os.system("clear")
'''
The asyncio module uses new style coroutines.  These are defined as a function prepended by the async keyword.
Coroutines are a type of generator and like generators you need to call them to create the actual coroutine.

The async/await keywords are introduced in Python 3.5 to make grammar of coroutine programming more meaningful.
These coroutines are slightly different from earlier coroutines in that they generate data but do not consume
data.  They are primary aimed at providing concurrency for IO based applications.
'''

import asyncio
import warnings

async def f():
    pass
    
#  async functions must be called to create a coroutine
print(f"f is of type: {type(f)}")

# coroutines generate a warning if not awaited
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    print(f"f() is of type: {type(f())}")

