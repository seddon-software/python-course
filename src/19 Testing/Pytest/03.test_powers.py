'''
only run tests in a given file
    i.e. mytests/test_power_functions.py

Note: all subdirectories contain "__init__.py"
'''

import os

os.system("pytest mytests/test_power_functions.py")
os.system("pytest mytests/test_power_functions.py --no-header")

