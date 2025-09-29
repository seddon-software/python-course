'''
When using pytest it is helpful to have separate "src" and "test" directories.

Note: pytest will not understand import statements unless you make both directories modules.  This means you should add empty "__init__.py" 
files to both "src" and "test" directories.

To install pytest use:
            pip install pytest --user

All the tests are in the folder "mytests"  We use os.system to simulate running tests from the command line.
'''

import os; os.system("clear")

print("all src and test directories must contain '__init__.py'")
os.system("tree ../src -I __pycache__")
os.system("tree mytests")

# only run tests in a given file
os.system("pytest mytests/test_point_class.py")

# clean up "pyc" files
os.system("find .. -name '*.pyc' -exec rm {} \;")

