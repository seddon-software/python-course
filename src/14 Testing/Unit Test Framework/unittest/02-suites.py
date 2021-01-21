from Point import *
import unittest


class testPoint(unittest.TestCase):
    """
    A test class for the Point class
    """

    def setUp(self):
        """
        set up data used in the tests.
        setUp is called before each test function execution.
        """
        self.point = Point(3, 4)

    def testConstructor(self):
        """constructor test"""
        self.assertEqual("3,4", self.point.display())

    def testMoveBy5and2(self):
        """moveBy test(1)"""
        self.point.moveBy(5, 2)
        self.assertEqual("8,6", self.point.display())
        
    def testMoveBy5and2version2(self):
        """moveBy test(2)"""
        self.point.moveBy(5, 2)
        self.assertEqual("8,7", self.point.display())

    def testDistanceIs5(self):
        """distance test(1)"""
        self.assertTrue(5 == self.point.get_distance())

    def testDistanceIs5_1(self):
        """distance test(2)"""
        self.assertTrue(5.1 == self.point.get_distance())

def suite():
    suite = unittest.TestSuite()
    suite.addTest(testPoint('testConstructor'))
    suite.addTest(testPoint('testMoveBy5and2'))
    suite.addTest(testPoint('testDistanceIs5'))
    print((str(suite.countTestCases()) + " test cases in suite"))
    return suite



if __name__ == '__main__':
#    import doctest

    mySuite = suite()
#    unittest.TextTestRunner(verbosity=0).run(mySuite)
#   unittest.TextTestRunner(verbosity=1).run(mySuite)
    unittest.TextTestRunner(verbosity=2).run(mySuite)

    1
    