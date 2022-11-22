import yaml
from yaml.loader import SafeLoader

salary = [{  
            "john":   34000,
            "sara":   27000,
            "pedro":  52000,
            "tim":    12500,
            "zoe":    66000,
          },
          {
            "Bill":   37000,
            "Jim":    44000,
            "Mary":   62000,
            "Viv":    42000,
          }]

OUTFILE = 'data/salaries_doc.yaml'

with open(OUTFILE, "w") as f:
    # g = yaml.load_all(f, Loader=SafeLoader)
    # data = list(g)
    yaml.dump_all(salary, f)

import os
os.system(f"cat {OUTFILE}")
