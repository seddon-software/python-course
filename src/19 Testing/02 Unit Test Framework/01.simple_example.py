from Point import *
import unittest


class testPoint(unittest.TestCase):
    """
    A class to test the Point class
    """

    def setUp(self):
        """
        set up data used in the tests.
        setUp is called before each test function execution.
        """
        self.point = Point(3, 4)

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
