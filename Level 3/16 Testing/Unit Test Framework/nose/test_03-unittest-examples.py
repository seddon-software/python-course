import unittest

class TestBasicAsserts(unittest.TestCase):
    def test_assertEqual(self):         self.assertEqual(5, 5)
    def test_assertNotEqual(self):      self.assertNotEqual(5, 6)
    def test_assertTrue(self):          self.assertTrue(5 < 6)
    def test_assertFalse(self):         self.assertFalse(5 > 6)
    def test_assertIs(self):            self.assertIs(5, 6 - 1)
    def test_assertIsNot(self):         self.assertIsNot(5, 6 + 1)
    def test_assertIsNone(self):        self.assertIsNone(None)
    def test_assertIsNotNone(self):     self.assertIsNotNone(1)
    def test_assertIn(self):            self.assertIn(5, [6, 8, 2, 5, 9])
    def test_assertNotIn(self):         self.assertNotIn(5, [6, 8, 2, 9])
    def test_assertIsInstance(self):    self.assertIsInstance(5, int)
    def test_assertNotIsInstance(self): self.assertNotIsInstance(5, float)

if __name__ == '__main__':
    unittest.main()
    
