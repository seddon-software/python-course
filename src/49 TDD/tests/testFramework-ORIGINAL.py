# add the src directory to the PYTHONPATH
import sys
sys.path.append("../src")

# import the source code: calculator.py
from  calculator import *

# setup the UnitTest framework
import unittest         # the standard module
from green_red import *     # user defined red/green extensions

# now for the tests
class testCalculator(unittest.TestCase):
    def setUp(self):
        pass

    # tests go in here
    pass

# start the tests with red/green color runner
if __name__ == '__main__':
    unittest.main(testRunner=ColorRunner())

