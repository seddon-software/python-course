# Mock is designed for use with unittest. 
# Mock is based on the 'action -> assertion' pattern instead 
# of 'record -> replay' used by many mocking frameworks.


import time
import unittest 
from unittest.mock import patch

'''This class is called by the class being tested, but we don't want to use the real class
because it may be unavailable, take too long to run in a unit test or have further dependencies 
that are not available.  So we mock out the methods used'''
class Shares:
    def __init__(self, name):
        self.name = name

    'This method is mocked out'
    def getPrice(self):
        # this method will do something complicated in practice
        # and we don't wan't it to take part in the test
        pass
 
class Market:
    'We are testing the following method which calls a mocked out method'
    def calculateChangeInSharePrice(self, share):
        startingPrice = share.getPrice()
        time.sleep(5)
        finishingPrice = share.getPrice()
        return finishingPrice - startingPrice
    
class testStocks(unittest.TestCase):
    'testing a method that calls a mocked out method'
    @patch.object(Shares, 'getPrice')
    def test_change_in_share_price(self, mocked_method):
        return_values= [31.2, 25.7]  # values in reverse order
        def side_effect():
            return return_values.pop()
        mocked_method.side_effect = side_effect
        ibm =  Shares("IBM")
        market = Market()
        change = market.calculateChangeInSharePrice(ibm)
        self.assertTrue(5.5 == change)


if __name__ == '__main__':
    unittest.main()
    
