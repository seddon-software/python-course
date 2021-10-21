############################################################
#
#       Type hints: Optional
#
############################################################

from typing import Optional

def compare(a:int, b:int, order:Optional[str]="ascending", **kwargs):
    if not order or order=="ascending":
        print(a)
    else:
        print(b)

try:
    compare(6, 7, None)
    compare(6, 7, "ascending")
    compare(6, 7, "descending")
    compare(6, 7)
except Exception as e:
    print(e)

############################################################
# now check the above code
############################################################

import os
print(f"mypy {os.path.basename(__file__)}")
os.system(f"mypy {os.path.basename(__file__)}")
