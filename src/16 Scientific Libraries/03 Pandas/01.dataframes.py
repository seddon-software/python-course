import os; os.system("clear")
'''
DataFrames
==========

Pandas 2D datasets are called dataframes.  In this example we read data from a file into a dataframe:
            lerwick_data = pd.read_csv("data/lerwick.txt", ...) 

Note that although we are using "read_csv()" the data file doen't have to be a set comma seperated data (although
this was the original idea).  This example shows several methods of the dataframe.

Parameters to "read_csv" include the engine, which can be "python" or "C" dependent on the authoring language;
the C engine is faster but less flexible.  We will use the Python engine in all our examples because unlike the 
C engine, it allows us to use RegExs when specify the field separated.  Normall Pandas will use the first row
to determine column names, but you can provide your own names by setting the "names" parameter.

The field seperator is the RegEx:
            '[*# ]+'
which means at least one of the characters in the [], i.e. * # or space, repeated in any order one or more times.

At the end of the example we show how to iterate through each row of the dataframe.
'''

import pandas as pd
pd.set_option('display.precision', 1)
pd.set_option('display.width', 80)
pd.set_option('display.max_rows', None) # None means all data displayed


def main(): 
    column_names = ['year', 'month', 'tmax', 'tmin', 'air-frost-days', 'rain(mm)', 'sun(hours)', 'comment']
    lerwick_data = pd.read_csv("data/lerwick.txt", 
                               skiprows = 7,
                               engine = 'python',
                               names = column_names, 
                               skipinitialspace = True, 
                               sep = '[*# ]+')
    print(lerwick_data)
    
    df = lerwick_data
    print(df.head())       # first five rows
    print(df.tail())       # last five rows
    print(df.sample(5))    # random sample of rows
    print(f"shape of dataframe: {df.shape}")        # number of rows/columns in a tuple

main()
