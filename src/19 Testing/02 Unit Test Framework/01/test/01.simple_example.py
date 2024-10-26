'''
The unittest unit testing framework was originally inspired by Java's JUnit.
It is important to isolate tests from the code under test to avoid test software ending up in released code.
In these examples we have the following directory structure:
            .
            ├── src
            │   ├── file_under_test1.py
            │   ├── file_under_test2.py
            │   └── file_under_test3.py
            └── test
                ├── test_file_under_test1.py
                ├── test_file_under_test2.py
                └── test_file_under_test3.py

Two further important points:
        1) Tests should have verbose highly descriptive file names
        2) Tests should define expected and actual test results in the form:
            assertEqual(expectedResult, actualResult)

Unit test has a variety of checks (see later), not just assertEqual
'''

import sys
sys.path.append("../src")

from Point import *
import unittest


class testPoint(unittest.TestCase):
    """
    A class to test the Point class
    """

    def setUp(self):
        """
        set up data used in the tests below.
        setUp is called before each test is executed.
        """
        self.point = Point(3, 4)            # this is called a test fixture

    def testWeCanDisplayCoordinatesOfFixture(self):
        """display test"""
        self.assertEqual("3,4", self.point.display())

    def testMoveFixtureBy5inXand2inY(self):
        """moveBy Point by X=5, Y=2"""
        self.point.moveBy(5, 2)
        self.assertEqual("8,6", self.point.display())
        
    def testMoveFixtureBy5inXand2inYusingBuggyMethod(self):
        """moveBy test using buggy method"""
        self.point.moveBy(5, 2)
        self.assertEqual("8,7", self.point.display())
        
    def testDistanceFromOriginIs5(self):
        """distance of fixture from origin is 5"""
        self.assertTrue(5 == self.point.get_distance())

    def testDistanceFromOriginIs5usingBuggyMethod(self):
        """distance test using buggy method"""
        self.assertTrue(5.1 == self.point.get_distance())


if __name__ == '__main__':
    unittest.main(exit=False)
