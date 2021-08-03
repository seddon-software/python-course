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

import os
os.system("mypy 07_optional_parameters.py")
