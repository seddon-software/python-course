'''
This is the same example as earlier, except we are using Polars to do the computations
'''

import pandas as pd
import polars as pl
import matplotlib.pyplot as plt
import numpy as np

    
def main():
    # set column names and read in data from file using pandas (because of the complicated field seperator)
    column_names = ['year', 'month', 'tmax', 'tmin', 'air-frost-days', 'rain(mm)', 'sun(hours)', 'comment']
    oxford_data = pd.read_csv("data/oxford_2022.txt", 
                              engine = 'python', 
                              skiprows = 7, 
                              names = column_names,     
                              na_values = ['---'], 
                              skipinitialspace = True, 
                              sep = '[*# ]+')

    oxford_data = pl.from_pandas(oxford_data)

    # drop columns we are not using (no inplace operations permitted)
    oxford_data = oxford_data.drop(['air-frost-days', 'rain(mm)', 'sun(hours)', 'comment'])

    # drop rows with missing data
    oxford_data = oxford_data.drop_nulls()

    # create a new column from year and month columns
    oxford_data = oxford_data.with_columns( ((pl.col('year')//4)*4).alias('period'))
    
    # group results into 4 year periods
    summary = oxford_data.group_by('period') \
                .agg([pl.col('tmin').mean().alias('tmin'), pl.col('tmax').mean().alias('tmax')]) \
                .sort(by='period')

    # convert back to pandas for plotting (we should use altair, but can't figure out how to do a dual plot)
    summary = summary.to_pandas()
    
    # plot the data
    ax = summary.plot(figsize=(10, 6), 
                               title = 'Oxford : Average Min and Max Temperatures (over 4 year periods)', 
                               x = 'period',
                               y = ['tmin', 'tmax'], 
                               color = ['red', 'green'], 
                               kind = 'bar')

    ax.set_xlabel("4 year period")
    ax.set_ylabel(f"{chr(0x2103)}")     # unicode ℃
    for item in [ax. title, ax.xaxis.label, ax.yaxis.label]:
        item.set_fontsize(20)
    plt.show()

main()



