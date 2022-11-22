'''
You can convert Python objects to YAML.  Here we work with a Python dict.
'''

import yaml
from yaml.loader import SafeLoader

salary = {
 		  "john":  34000, 
          "sara":  27000,
          "pedro": 52000,
          "tim":   12500,
          "zoe":   66000
         }

OUTFILE = 'data/salaries.yaml'
with open(OUTFILE, 'w') as f:
    # don't sort keys => insertion order used
    yaml.dump(salary, f, sort_keys=False, default_flow_style=False)

import os
os.system(f"cat {OUTFILE}")
