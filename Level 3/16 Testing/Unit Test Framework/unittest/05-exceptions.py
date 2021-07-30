import unittest

class MyException(Exception): pass
    

def f(x, y): 
    if x == y: raise MyException("args must not be equal" + str(x))
    return (x * y) / (x - y)

class TestExceptions(unittest.TestCase):
    def testMyExceptionIsRaisedByCallingFWithTwoParametersThatAreEqual(self):
        self.assertRaises(MyException, f, 6, 6)
        
    def testWhatHappensIfMyExceptionIsNotRaised(self):
        self.assertRaises(MyException, f, 6, 3)
        
    def testMyExceptionIsRaisedWithCorrectMessage(self):
        self.assertRaisesRegex(MyException, 'args must not be equal.*', f, 6, 6)

if __name__ == '__main__':
    unittest.main()
    
