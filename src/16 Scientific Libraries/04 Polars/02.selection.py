'''
Common Pandas Selection Operations
==================================

In this example we use a small dataset to illustrate common Pandas operations.  Note that Pandas defines two
key types:
    dataframe:       2D table
    series:          1D table

Pay special attention as to which data type is return from the operations below; further operations on dataframes
and series are very different.

Note there are 3 distinct ways of interacting with dataframes:
    1) direct       df.             ...
    2) loc          df.loc          use index to select data
    3) iloc         df.iloc         use numerical index to select data
'''

import os; os.system("clear")
import pandas as pd
import polars as pl
#import matplotlib.pyplot as plt
pd.set_option('display.precision', 1)
pd.set_option('display.width', None)        # None means all data displayed
pd.set_option('display.max_rows', None)

def inspect(item):
    print()
    print(item)
    print(type(item))
    print("-"*len(str(type(item))))  # print underscores

def main(): 
    # seperator has to be a single character
    df = pl.read_csv("data/polars_sample.txt", skip_rows=0, skip_rows_after_header=1, separator='\t')
    try:
        df = df.with_row_index("Name")
    except Exception as e:
        print(e)
    print(df)

    # the schema
    inspect(df.schema)
    
    # # the values of the dataset (Numpy arrays)
    # inspect(df.to_numpy())
    # inspect(df.to_numpy()[0])
    # inspect(df.to_numpy()[0, 0])

    # extracting a single column can create a new dataframe or a series
    inspect(df.select('County'))    # [[list parameter]] => returns a dataFrame
    inspect(df['County'])      # [scalar parameter] => returns a series
        
    # using .loc
    # loc uses the index of the dataset.  A lot of datasets have an index of
    # integers, but the index can be any data type, often str
    
    # print 1 row
    inspect(df.loc['Peter'])   # loc uses index

    # print several rows
    inspect(df.loc['Peter':'Bill'])

    # selecting rows and columns
    inspect(df.loc[['Peter', 'Bill'], ['County', 'Height', 'Weight']])
    inspect(df.loc[:, ['County', 'Gender']])  # all rows, some columns
    inspect(df.loc[['Bill'], ['County']])     # 1 row, 1 column, two sets of []
    inspect(df.loc['Bill', 'County'])         # only 1 set of []

    # remind ourselves of the complete dataframe
    print(df)

    # using iloc
    # iloc uses the numerical index of the dataset, starting with item 0
    inspect(df.iloc[3])              # select row 3 as series
    inspect(df.iloc[[3, 6, 2, 4]])   # select multiple rows
    inspect(df.iloc[3, 2])           # select row and column

    # convert the index to a regular column
    # the new index will be numerical
    df.reset_index(inplace=True)
    print(df)
main()
