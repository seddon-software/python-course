############################################################
#
#       Type hints: valid code
#
############################################################

def average(x:float, y:float, z:float) -> float:
    return (x + y + z)/3.0

print(average(5.5, 7.7, 9))

#):
############################################################
# now check the above code
############################################################

import os
print(f"mypy {os.path.basename(__file__)}")
os.system(f"mypy {os.path.basename(__file__)}")
