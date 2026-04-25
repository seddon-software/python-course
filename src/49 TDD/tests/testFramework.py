# add the src directory to the PYTHONPATH
import sys
sys.path.append("../src")

# import the source code: calculator.py
from  calculator import *
c = Calculator()

# setup the UnitTest framework
import unittest         # the standard module
from green_red import *     # user defined red/green extensions

# now for the tests
class testCalculator(unittest.TestCase):
    def setUp(self):
        c = Calculator()

    # tests go in here
    def test_Add_One_and_Two(self):
        actual = c.add(1,2)
        expected = 3
        self.assertEqual(expected, actual)

    def test_Add_15_and_32(self):
        actual = c.add(15, 32)
        expected = 47
        self.assertEqual(expected, actual)

    def test_with_bad_LHS(self):
        with self.assertRaises(BadInput) as context:
            c.add('xxx', 32)
            print("Exception message:", context.exception)

    def test_with_bad_RHS(self):
        with self.assertRaises(BadInput):
            c.add(32, 'xxx')
    
    def test_with_floats(self):
        actual = c.add(15.1, 32.9)
        expected = 48.0
        self.assertEqual(expected, actual, f"Failed: got {actual}, expected {expected}")



# start the tests with red/green color runner
if __name__ == '__main__':
    unittest.main(testRunner=ColorRunner(), verbosity=3)

