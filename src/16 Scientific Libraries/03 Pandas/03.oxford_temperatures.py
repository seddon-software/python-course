'''
Oxford Temperatures
===================

This example analyses temperatures in Oxford (as downloaded from the Met Office site).  Because the dataset
is quite long (over 1000 records) we can't simply plot each entry (not enough room on the plot).  The
compromise is to aggregate all rows in a 4 year period and plot the average values of tmax and tmin.  

Note there are only two tricky bits in this example.

1)    oxford_data['period'] = oxford_data.apply(
        lambda row : (row['year']//4)*4, raw = False, 
        axis = 1
        )
 
Here we create a new column using the "apply()" method.  The "apply()" method takes 3 parameters; the first 
parameter is a function object that is called for each row in the dataset.  If raw=True, each row is passed 
as a Series (i.e. column name and value), but we are using raw=False which passes each row as a list of 
values; axis=1 means we are operating on rows rather than columns.

The lambda takes an input row, selects the year column (row['year']) and performs an integer division by 4.
The integer division ignore remainders, so when we subsequently multiply by 4 we obtain a number divisible by 4.
The new column ('period') is therefore a multiple of 4 years.  For example:
    1951 -> 1948
    1952 -> 1952
    1953 -> 1952
    1954 -> 1952
    1955 -> 1952
    1956 -> 1956

2)    summary = oxford_data.groupby(['period']).aggregate(np.mean)

This uses our new column and groups all the rows with the same period and the takes the mean of the selected 
rows.  Since the original data is presented with the average max and min temperatures on a monthly basis there 
will be 48 rows with the same value of column (unless some data is missing).  The result is a new dataframe 
(summary) with far fewer rows ans suitable for plotting.
'''

import pandas as pd
import pylab as pl
import numpy as np
pd.set_option('display.precision', 1)
pd.set_option('display.width', 100)

    
def main(): 
    # set column names and read in data from file
    column_names = ['year', 'month', 'tmax', 'tmin', 'air-frost-days', 'rain(mm)', 'sun(hours)', 'comment']
    oxford_data = pd.read_csv("data/oxford.txt", 
                              engine = 'python', 
                              skiprows = 7, 
                              names = column_names, 
                              na_values = ['---'], 
                              skipinitialspace = True, 
                              sep = '[*# ]+')

    # some of the tmin values are missing, so drop these rows
    oxford_data.dropna()
    
    # create a new column from year and month columns
    oxford_data['period'] = oxford_data.apply(
        lambda row : (row['year']//4)*4, raw = False, 
        axis = 1
        )
    
    # look at some of the records with the new column added
    print(oxford_data.iloc[100:150])

    # drop columns we are not using (not necessary)
    oxford_data.drop(['year', 'month', 'air-frost-days', 'rain(mm)', 'sun(hours)', 'comment'], axis = 1, inplace = True)

    # look at some of the records now unused columns dropped
    print(oxford_data.iloc[100:150])

    # group results into 4 year periods
    # the groupby column (period) becomes the index
    summary = oxford_data.groupby(['period']).aggregate(np.mean)
    print(summary)

    # plot the data
    ax = summary.plot(figsize=(10, 6), 
                               title = 'Oxford : Average Min and Max Temperatures (over 4 year periods)', 
                               # x defaults to index
                               y = ['tmin', 'tmax'], 
                               color = ['red', 'green'], 
                               kind = 'bar')

    ax.set_xlabel("4 year period")
    ax.set_ylabel(f"{chr(0x2103)}")     # degrees C
    for item in [ax. title, ax.xaxis.label, ax.yaxis.label]:
        item.set_fontsize(20)
    pl.show()


main()



