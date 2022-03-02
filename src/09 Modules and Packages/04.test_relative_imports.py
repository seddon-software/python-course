'''app/
   __init__.py
   sub1/
      __init__.py
      mod1.py
   sub2/
      __init__.py
      mod2.py
'''

import sys
sys.path.append("mylib2")

print(__name__)
import app.sub1.module1 as m1


