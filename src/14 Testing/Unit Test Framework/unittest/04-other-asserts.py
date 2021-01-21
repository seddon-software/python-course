import unittest

class TestBasicAsserts(unittest.TestCase):
    def test_assertAlmostEqual(self):        self.assertAlmostEqual(5.0, 5.001, 2)
    def test_assertNotAlmostEqual(self):     self.assertNotAlmostEqual(5, 5.006,2)
    def test_assertGreater(self):            self.assertGreater(6, 5)
    def test_assertGreaterEqual(self):       self.assertGreaterEqual(5, 5)
    def test_assertLess(self):               self.assertLess(5, 6)
    def test_assertLessEqual(self):          self.assertLessEqual(5, 5)
    def test_assertRegexpMatches(self):      self.assertRegex("book", "b.+k")
    def test_assertNotRegexpMatches(self):   self.assertNotRegexpMatches("bk", "b.+k")
    def test_assertItemsEqual(self):         self.assertItemsEqual((3,5,4,2), [2,5,3,4])
    dict1 = {'a':2, 'b':4, 'c':6 }
    dict2 = {'a':2, 'c':6 }
    def test_problemWithAssertDictContainsSubset(self): 
                                             self.assertDictContainsSubset(self.dict1, self.dict2)
    def test_assertDictContainsSubset(self): self.assertDictContainsSubset(self.dict2, self.dict1)

if __name__ == '__main__':
    unittest.main()
    
