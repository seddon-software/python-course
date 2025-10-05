'''
pytest will run all files of the form test_*.py or *_test.py in the current directory and its subdirectories
unless you explicitly specify a test file (as in this example)

When using pytest it is helpful to have separate "src" and "test" directories.

Note: pytest will not understand import statements unless you make both directories modules.  This means you should add empty "__init__.py" 
files to both "src" and "test" directories.

To install pytest use:
            pip install pytest --user

All the tests are in the folder "mytests"  We use os.system to simulate running tests from the command line.
'''

import os; os.system("clear")

print("all src and test directories must contain '__init__.py'")

print("files under test")
os.system("tree ../src -I __pycache__")     # ignore pyc files

print("test files")
os.system("tree mytests -I __pycache__")

# look at the tests
os.system("clear")
os.system("cat mytests/test_Point.py")

# run tests
os.system("clear")
os.system("pytest mytests/test_Point.py")

