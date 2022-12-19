'''
Mock is designed for use with unittest. 
Mock is based on the 'action -> assertion' pattern instead of 'record -> replay' used by many mocking frameworks.

In this example we are testing the method:
            calculateChangeInSharePrice()

in the class
            Market

However, this method calls the 'getPrice' method of the 'Shares' class, but the 'getPrice' method is unavailable 
at the time of testing.  We can get round this by mocking out the 'getPrice' method.  There are various ways
to achieve this.
  
Here we define the 'side_effect' property of the class being mocked as a reference to our own routine that simply 
returns successive results.  
'''


import time
import unittest 
from unittest.mock import patch

# This class is called by the class being tested, but we don't want to use the real class because it 
# may be unavailable, take too long to run in a unit test or have further dependencies that are not available.  
# So we mock out the methods used

# this class is called indirectly and contains the mocked out method
class Shares:
    def __init__(self, name):
        self.name = name

    'This method is mocked out'
    def getPrice(self):
        # this method is not yet available (but will do something complicated in practice)
        # and hence we don't want it to take part in the unit test
        pass
 
# We are testing this class
class Market:
    # We are testing the following method, which calls a mocked out method'
    def calculateChangeInSharePrice(self, share):
        startingPrice = share.getPrice()    # call mocked out method
        time.sleep(5)
        finishingPrice = share.getPrice()   # call mocked out method
        return finishingPrice - startingPrice
    
# The test(s) follow:
class testStocks(unittest.TestCase):
    'testing a method that calls a mocked out method'
    @patch.object(Shares, 'getPrice')
    def test_change_in_share_price(self, mocked_getPrice):
        return_values= [31.2, 25.7]  # values will get popped (in reverse order)
        def side_effect():
            return return_values.pop()
        # mock out getPrice using 'side_effect@ property 
        mocked_getPrice.side_effect = side_effect
        ibm =  Shares("IBM")
        market = Market()
        change = market.calculateChangeInSharePrice(ibm)
        self.assertTrue(5.5 == change)

if __name__ == '__main__':
    unittest.main(exit=False)
    
