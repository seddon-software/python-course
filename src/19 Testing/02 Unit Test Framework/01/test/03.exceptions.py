'''
It is important to be able to check that code can raise an exception under certain conditions.
In this example we create a fixture of a distantPoint.  When we call the "distance" method, the method
should throw a TooFarException.
'''

import sys
sys.path.append("../src")

from Point import TooFarException
from Point import *
import unittest

import os
os.system("clear")

class testPoint(unittest.TestCase):
    """
    A class to test the Point class
    """

    def setUp(self):
        """
        set up data used in the tests below.
        setUp is called before each test is executed.
        """
        # these are called test fixtures
        self.point = Point(3, 4)
        self.distantPoint = Point(16, 4)

    # def testWeCanDisplayCoordinatesOfFixture(self):
    #     """display test"""
    #     self.assertEqual("3,4", self.point.display())

    # def testMoveFixtureBy5inXand2inY(self):
    #     """moveBy Point by X=5, Y=2"""
    #     self.point.moveBy(5, 2)
    #     self.assertEqual("8,6", self.point.display())
        
    # def testMoveFixtureBy5inXand2inYusingBuggyMethod(self):
    #     """moveBy test using buggy method"""
    #     self.point.moveBy(5, 2)
    #     self.assertEqual("8,7", self.point.display())
        
    # def testDistanceFromOriginIs5(self):
    #     """distance of fixture from origin is 5"""
    #     self.assertTrue(5 == self.point.get_distance())

    # def testDistanceFromOriginIs5usingBuggyMethod(self):
    #     """distance test using buggy method"""
    #     self.assertTrue(5.1 == self.point.get_distance())

    # these next two test show alternative ways of testing that exceptions are raised correctly
    def test_ExceptionRaisedWhen_get_distance_IsCalledFor_distantPoint(self):
        '''distantPoint.get_distance() should raise a TooFarException'''
        print()
        self.assertRaises(TooFarException, self.distantPoint.get_distance)

    def test_ExceptionRaisedWhen_get_distance_IsCalledInWithClauseFor_distantPoint(self):
        '''using a with clause to show distantPoint.get_distance() should raise a TooFarException'''
        print()
        with self.assertRaises(TooFarException) as ctx:
            self.distantPoint.get_distance()

    # this test will intentionally fail since point is close to the origin
        
    def test_ExceptionRaisedWhen_get_distance_IsCalledFor_point(self):
        '''this test will intentionally fail since point is close to the origin'''
        print()
        with self.assertRaises(TooFarException) as ctx:
            self.point.get_distance()



if __name__ == '__main__':
    # unittest.main(verbosity=0)
    # unittest.main(verbosity=1)
    unittest.main(verbosity=2)
