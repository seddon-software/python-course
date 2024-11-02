import os

# only run tests in a given file
# Note all subdirectories contain "__init__.py"
os.system("pytest mytests/test_power_functions.py --no-header")

