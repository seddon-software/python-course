# Reading Excel files requires the xlrd library. 
# You can install it via pip (pip install xlrd).

import pandas as pd
import pylab as pl
pd.set_option('display.precision', 1)
pd.set_option('display.width', 100)

def main(): 
    column_names = ['year', 'month', 'tmax', 'tmin', 'air-frost-days', 'rain(mm)', 'sun(hours)', 'comment']
    lerwick_data = pd.read_csv("data/lerwick.txt", 
                               skiprows = 8, 
                               names = column_names, 
                               skipinitialspace = True,
                               engine = 'python', 
                               sep = '[*# ]+')
    lerwick_data.to_excel('data/lerwick.xlsx', index = False)
    del lerwick_data
    lerwick_data = pd.read_excel('data/lerwick.xlsx', 'Sheet1')
    print(lerwick_data)

main()

