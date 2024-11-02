'''
We can use the -m command line option to only run tests with a given mark
'''

import os

# only run tests with a given mark
os.system("pytest -m intended_to_fail")

