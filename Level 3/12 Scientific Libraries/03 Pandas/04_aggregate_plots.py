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
        lambda row : (row.year//4)*4, raw = False, 
        axis = 1
        )

    # drop columns we are not using (not necessary)
    oxford_data.drop(['year', 'month', 'air-frost-days', 'rain(mm)', 'sun(hours)', 'comment'], axis = 1, inplace = True)

    # group results into 4 year periods
    # the groupby column (period) becomes the index
    summary = oxford_data.groupby(['period']).aggregate(np.mean)

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



