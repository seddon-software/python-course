# Mock is designed for use with unittest. 
# Mock is based on the 'action -> assertion' pattern instead 
# of 'record -> replay' used by many mocking frameworks.


import unittest 
from unittest.mock import patch

'''This class is called by the class being tested, but we don't want to use the real class
because it may be unavailable, take too long to run in a unit test or have further dependencies 
that are not available.  So we mock out the methods used'''
class MyClass():
    'This method is mocked out'
    def my_method(self):
        # this method will do something complicated in practice
        # and we don't wan't it to take part in the test
        pass
 
class ClassUnderTest():
    'We are testing this method (f) which calls the mocked out method'
    def f(self):
        myclass = MyClass()
        return myclass.my_method()
    
''' This is the unit test'''
class testPoint(unittest.TestCase):
    'testing a method mocked out with a constant return value (True)'
    @patch.object(MyClass, 'my_method')
    def test_that_f_returns_true_if_called_only_once(self, mocked_method):
        mocked_method.return_value=True # make the mock return True when called
        o =  ClassUnderTest()
        result = o.f()
        self.assertTrue(result)

    'testing a method mocked out which returns the successive results (False, False, True)'
    @patch.object(MyClass, 'my_method')
    def test_that_f_returns_False_False_True_on_successive_calls(self, mocked_method):
        return_values= [False,False,True]
        def side_effect():
            return return_values.pop()
        mocked_method.side_effect = side_effect # make the mock return False, False, True on successive calls

        o =  ClassUnderTest()
        self.assertTrue(o.f())
        self.assertFalse(o.f())
        self.assertFalse(o.f())

if __name__ == '__main__':
    unittest.main()
    1
