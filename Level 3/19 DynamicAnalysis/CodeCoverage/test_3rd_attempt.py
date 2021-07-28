#!/usr/bin/env python

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

    def test_multiply_operation(self):
        result = process_input(self.a, self.b, "multiply")
        self.assertEqual(result, 50)

    def test_divide_operation(self):
        result = process_input(self.a, self.b, "divide")
        self.assertEqual(result, 2)

def suite():
    "Test suite"
    suite = unittest.TestSuite()

    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestApp))
    return suite

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(suite())
    print("all tests completed")
    os.system("coverage run test_3rd_attempt.py")

