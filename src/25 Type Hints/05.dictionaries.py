'''
dictionaries
============
This time we are working with dictionaries.  We give two examples of calling our function 'sum_values', one
with correct types and one with incorrect types.  The second call raises an exception at runtime; mypy will 
report on what is wrong.
'''

############################################################
# 1) run the program
############################################################

def sum_values(d:dict[str,int]) -> int:
    return sum([d[key] for key in d])

salary = { "john":  34000,  "sara":  27000, "pedro": 52000, "tim":   12500, "zoe":   66000 }
names = { "john": "brown", "sara": "smith", "pedro": "phillipe", "tim": "tonka", "zoe": "zidane" }

try:
    print(sum_values(salary))   # ok, salary is dict[str,int]  
    print(sum_values(names))    # names is not dict[str,int]
except Exception as e:
    print(f"Exception: {e}")

############################################################
# 2) perform static analysis with Mypy
############################################################
import os
print(f"mypy {os.path.basename(__file__)}")
os.system(f"mypy {os.path.basename(__file__)}")

