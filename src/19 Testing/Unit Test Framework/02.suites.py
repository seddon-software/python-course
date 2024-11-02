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
        
    def testDistanceFromOriginIs5(self):
        """distance of fixture from origin is 5"""
        self.assertTrue(5 == self.point.get_distance())

    def testMoveFixtureBy5inXand2inYusingBuggyMethod(self):
        """moveBy test using buggy method"""
        self.point.moveBy(5, 2)
        self.assertEqual("8,7", self.point.display())
        
    def testDistanceFromOriginIs5usingBuggyMethod(self):
        """distance test using buggy method"""
        self.assertTrue(5.1 == self.point.get_distance())

def suite():
    suite = unittest.TestSuite()
    suite.addTest(testPoint('testWeCanDisplayCoordinatesOfFixture'))
    suite.addTest(testPoint('testMoveFixtureBy5inXand2inY'))
    suite.addTest(testPoint('testDistanceFromOriginIs5'))
    print((str(suite.countTestCases()) + " test cases in suite"))
    return suite



if __name__ == '__main__':
    mySuite = suite()
#    unittest.TextTestRunner(verbosity=0).run(mySuite)
#    unittest.TextTestRunner(verbosity=1).run(mySuite)
    unittest.TextTestRunner(verbosity=2).run(mySuite)



# if __name__ == '__main__':
#     unittest.main(exit=False)
