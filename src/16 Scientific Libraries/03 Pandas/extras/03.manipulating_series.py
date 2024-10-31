import pandas as pd
import numpy as np


def title(t):
    print("\n")
    print(t)
    print("=" * len(t))

pd.set_option('display.width', 1000)
pd.set_option('display.precision', 2)

##########
title("create a series with different indices")
s1 = pd.Series(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'], index=['A', 'B', 'C', 'D', 'E'])
print(s1, end="\n\n")
s2 = pd.Series(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'], index=range(10, 20, 2))
print(s2, end="\n\n")

##########
title("create a series from a dict")
d = { "john"  : 34000, 
      "sara"  : 27000,
      "pedro" : 52000,
      "tim"   : None,
      "zoe"   : 66000 }

salaries = pd.Series(d)
print(salaries)

##########
title("select from series")
print(salaries[["sara", "pedro", "zoe"]])
print(f"john's salary: {salaries.john}")
print(salaries[salaries < 40000])

##########
title("modifying series")
print('Old value:', salaries['tim'])
salaries['tim'] = 41000
print('New value:', salaries['tim'])

##########
title("modifying series using predicates")
# changing values using boolean logic
salaries[salaries < 45000] = 25000
print(salaries[salaries < 26000])

##########
title("check if item present in series")
print('john' in salaries)
print('mary' in salaries)

##########
title("perform operations on series")
# divide salaries values by 3
print(salaries / 3)

##########
title("add series together")
s1 = salaries[['john', 'pedro']]
print(f"s1:\n{s1}\n")
s2 = salaries[['zoe']]
print(f"s2:\n{s2}\n")
s = s1.add(s2, fill_value=0)
print(f"s1.add(s2):\n{s}\n")

##########
title("check for non-nulls in series")
salaries['mary'] = None
print(salaries.notnull())
title("check for nulls in series")
print(salaries.isnull())
print(salaries[salaries.isnull()])
