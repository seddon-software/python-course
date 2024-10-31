'''
Read and Write Excel
====================
Pandas makes it easy to read and write to Excel files with the methods:
            lerwick_data.to_excel('data/lerwick.xlsx', index = False)
            lerwick_data = pd.read_excel('data/lerwick.xlsx', 'Sheet1')

Note: Working with Excel files requires the xlrd library.  You can install it via pip:
            pip install xlrd --user
'''

import pandas as pd
import pylab as pl
import openpyxl
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
    # write to the spreadsheet
    lerwick_data.to_excel('data/lerwick.xlsx', index = False)

    # delete the dataframe in memory
    del lerwick_data

    # check we can read back the dataframe from the spreadsheet
    lerwick_data = pd.read_excel('data/lerwick.xlsx', 'Sheet1')
    print(lerwick_data)

main()

