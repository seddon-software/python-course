############################################################
#
#       Type hints: invalid code
#
############################################################

def concat(x:str, y:str, z:str) -> str:
    result = x + y + z

print(concat(5, 7, 9))

#):
############################################################
# now check the above code
############################################################

import os
print(f"mypy {os.path.basename(__file__)}")
os.system(f"mypy {os.path.basename(__file__)}")

