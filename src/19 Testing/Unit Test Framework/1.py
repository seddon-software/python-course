# add the src directory to the PYTHONPATH
import sys
sys.path.append("../src")

# import the source code
from leapYears import *

# setup the UnitTest framework
import unittest         # the standard module
from green_red import *     # user defined red/green extensions

# now for the tests
class testPoint(unittest.TestCase):
    def test_2016_is_a_leap_year(self):
        self.assertTrue(isLeap(2016))
    def test_2017_is_not_leap_year(self):
        self.assertFalse(isLeap(2017))
    def test_2018_is_not_leap_year(self):
        self.assertFalse(isLeap(2018))
    def test_2027_is_not_leap_year(self):
        self.assertFalse(isLeap(2027))
    def test_2024_is_a_leap_year(self):
        self.assertTrue(isLeap(2024))
    def test_1900_is_not_leap_year(self):
        self.assertTrue(isLeap(1900))

# start the tests with red/green color runner
if __name__ == '__main__':
    unittest.main(testRunner=ColorRunner())
