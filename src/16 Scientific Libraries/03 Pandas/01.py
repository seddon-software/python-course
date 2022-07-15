'''
Find year with lowest sun(hours)
'''

import pandas as pd
import pylab as pl
import numpy as np
pd.set_option('display.precision', 1)
pd.set_option('display.width', 100)

    
def main(): 
    # set column names and read in data from file
    column_names = ['year', 'month', 'tmax', 'tmin', 'air-frost-days', 'rain(mm)', 'sun(hours)', 'comment']
    oxford_data = pd.read_csv("data/oxford_2022.txt", 
                              engine = 'python', 
                              skiprows = 7, 
                              names = column_names, 
                              na_values = ['---'], 
                              skipinitialspace = True, 
                              sep = '[*# ]+')
    # remove rows with missing data
    oxford_data.dropna(subset=['sun(hours)'],inplace=True)

    # select only August data
    temperatures = oxford_data.query('month==8')[['year', 'sun(hours)']]

    # find minimum temperature
    minTemperature = temperatures[temperatures['sun(hours)'] == temperatures['sun(hours)'].min()]
    print(minTemperature.to_string(index=False))
main()
