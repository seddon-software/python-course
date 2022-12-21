import sys
sys.path.append("../src")

import os, unittest
from mycode import process_input

class TestApp(unittest.TestCase):
    """Test the mathematical operations"""

    def setUp(self):
        "This runs before the test cases are executed"
        self.a = 10
        self.b = 5

    def test_add_operation(self):
        result = process_input(self.a, self.b, "add")
        self.assertEqual(result, 15)

    def test_subtract_operation(self):
        result = process_input(self.a, self.b, "subtract")
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main(exit=False)


