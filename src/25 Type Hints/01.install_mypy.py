'''
Install Mypy
============
Mypy is an static type checker for Python and will use type hints to validate programs.  Mypy should already 
be available at DLS, but on other systems you can install with:
            sudo apt install mypy

Once Mypy is installed, you can install the Python interface to Mypy with this script.
'''

import os

# this installs the python interface to mypy
os.system("python -m pip install mypy --user")
