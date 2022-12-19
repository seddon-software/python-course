import os

# only run tests in a given file
# Note all subdirectories contain "__init__.py"
os.system("pytest mytests/test_Point_class.py --no-header")

