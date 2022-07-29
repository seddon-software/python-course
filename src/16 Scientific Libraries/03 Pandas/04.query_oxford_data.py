'''
Query Oxford Data
=================

Say we wan to find year with lowest number of sun(hours) in the month of August.  Last year was the worst year in 
the last 90.  Or at least it was until the Met Office revised it's data at the begining of this year.  Let's find
the new year with the worst August sunshine using Pandas.

The Pandas query method os ideally suited to this task.  We can query our dataframe with
            oxford_data.query('month==8')

to select a new dataframe consisting of rows with the month equal to 8.  If we further reduce the dataset with the
selection: 
            [['year', 'sun(hours)']]

we get another dataset (because of two sets of []) with just the two columns specified.

Finally, we select the one row where
            sun(hours) == 'sun(hours)'.min()

using the statement:
            minTemperature = temperatures[temperatures['sun(hours)'] == temperatures['sun(hours)'].min()]

In the final print out we use the values of the two columns with the index removed.  The easiest way of doing 
this is to create a series and then convert to a Numpy array, remembering to take element [0].
            year = minTemperature['year'].values[0]
            sunshine = minTemperature['sun(hours)'].values[0]
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
    temperatures = oxford_data.query('month==8')
    print(temperatures)
    temperatures = oxford_data.query('month==8')[['year', 'sun(hours)']]

    # find minimum temperature
    minTemperature = temperatures[temperatures['sun(hours)'] == temperatures['sun(hours)'].min()]

    year = minTemperature['year'].values[0]
    sunshine = minTemperature['sun(hours)'].values[0]
    print(f"Least sunshine in August was in {year} with {sunshine} hours of sun")
main()
