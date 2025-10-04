'''
In this example we test a different file:
    powers.py
'''

import os

# look at the tests
os.system("cat mytests/test_powers.py")

# os.system("pytest mytests/test_powers.py")
os.system("pytest mytests/test_powers.py --no-header")

