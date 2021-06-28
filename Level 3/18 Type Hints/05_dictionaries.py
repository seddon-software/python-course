def sum_values(d:dict[str,int]):
    return sum([d[key] for key in d])



salary = {
 		  "john":  34000, 
          "sara":  27000,
          "pedro": 52000,
          "tim":   12500,
          "zoe":   66000
         }
names = {
 		  "john":  "brown", 
          "sara":  "smith",
          "pedro": "phillipe",
          "tim":   "tonka",
          "zoe":   "zidane"
         }


try:
    print(sum_values(salary))
    print(sum_values(names))
except Exception as e:
    print(e)

import os
os.system("mypy 05_dictionaries.py")
