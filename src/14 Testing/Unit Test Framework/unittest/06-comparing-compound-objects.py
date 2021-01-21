import unittest

class TestBasicAsserts(unittest.TestCase):
    def test_assertMultiLineEqual(self): self.assertMultiLineEqual(str1, str2)
    def test_assertSequenceEqual(self):  self.assertSequenceEqual(seq1, seq2)
    def test_assertListEqual(self):      self.assertListEqual(list1, list2)
    def test_assertTupleEqual(self):     self.assertTupleEqual(tuple1, tuple2)
    def test_assertSetEqual(self):       self.assertSetEqual(set1, set2)
    def test_assertDictEqual(self):      self.assertDictEqual(dict1, dict2)

str1 = '''
    line1
    line2a
    line3
'''
str2 = '''
    line1
    line2
    line3
'''
seq1 = 3, 6, 2, 8
seq2 = 3, 5, 1, 8
tuple1 = (3, 6, 2, 8)
tuple2 = (3, 5, 1, 8)
list1 = [3, 6, 2, 8]
list2 = [3, 5, 1, 8]
set1 = set(seq1)
set2 = set(seq2)
dict1 = {'a':1,'b':2,'c':3}
dict2 = {'a':1,'d':0,'c':3}

if __name__ == '__main__':
    unittest.main()




