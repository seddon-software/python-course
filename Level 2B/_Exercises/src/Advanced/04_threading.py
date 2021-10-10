############################################################
#
#    Threading Exercise
#
############################################################

import random
import time
import sys

from threading import Thread
from threading import Event

class Share:
    # prices are stored in an internal list
    
    def __init__(self, startPrice):
        '''set up initial list of prices'''
        self.prices = [int(startPrice)]

    def nextPrice(self):
        '''generate a new share price'''
        
        # simulate taking some time to get a new share price
        time.sleep(0.01 * random.random())

        # calculate change in price and append to list
        delta = int(random.random() * 100 - 50)
        currentPrice = self.prices.pop() # easy way to get last price
        self.prices.append(currentPrice) # must push it back again
        currentPrice += delta
        self.prices.append(currentPrice) # append new price
        
    def getPrices(self):
        '''get list of recent prices''' 
        prices = self.prices
        currentPrice = self.prices.pop()
        self.prices = [currentPrice]
        return prices # return list as it was before reset
    
    def reset(self):
        '''reset list of prices'''
        currentPrice = self.prices.pop()
        self.prices = [currentPrice]



def ticker(company):
    global pricesAvailableEvent
    global resetEvent

    def getPrices(count):
        for i in range (1, count):
            company.nextPrice()
        
    for i in range (1, 25):
        pricesAvailableEvent.wait()
        pricesAvailableEvent.clear()
        getPrices(10)
        resetEvent.set()


def monitor(company):
    global pricesAvailableEvent
    global resetEvent

    def Average(myPrices):
        total = 0
        count = myPrices.__len__()
        for price in myPrices:
            total += price
        return total/count
        
    for i in range (1, 25):
        resetEvent.wait()
        resetEvent.clear()
        print(f"{Average(company.getPrices()):.2f}")
        company.reset()
        pricesAvailableEvent.set()


mycompany = Share(10000)
pricesAvailableEvent = Event()
resetEvent = Event()

thread1 = Thread(target=ticker, args=((mycompany,)))
thread2 = Thread(target=monitor, args=((mycompany,)))

thread1.start()
thread2.start()

pricesAvailableEvent.set()

thread1.join()
thread2.join()

print("\nEnd of main Thread") 



