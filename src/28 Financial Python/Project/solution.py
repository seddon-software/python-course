import pandas as pd
import pylab as pl
import numpy as np
import openpyxl as xl
from _sqlite3 import Row

pd.set_option('display.precision', 1)
pd.set_option('display.width', 100)
    
def main(): 
    prices = pd.read_excel("StockPrices.xlsx")
    prices['Nike-prev'] = prices['Nike'].shift()
    prices['Apple-prev'] = prices['Apple'].shift()
    def logReturn(row, name):
        name_prev = name + '-prev'
        try:
            return np.log(row[name]/row[name_prev])
        except:
            return np.NaN
    prices['Nike-log-return'] = prices.apply(logReturn, raw = True, axis = 1, args = ['Nike'])
    prices['Apple-log-return'] = prices.apply(logReturn, raw = True, axis = 1, args = ['Apple'])
    prices['Date'] = prices['Date'].dt.strftime('%d:%m')
    print(prices)
    ax = prices[-50:].plot(figsize=(10, 6), 
                               title = 'Shares', 
                               # x defaults to index
                               x = ['Date'],
                               y = ['Nike-log-return', 'Apple-log-return'], 
                               color = ['red', 'cyan'], 
                               kind = 'bar')
    pl.show()

    


main()



