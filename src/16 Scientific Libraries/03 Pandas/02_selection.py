import os; os.system("clear")
import pandas as pd
import pylab as pl
pd.set_option('display.precision', 1)
pd.set_option('display.width', None)        # None means all data displayed
pd.set_option('display.max_rows', None)

def inspect(item):
    print()
    print(item)
    print(type(item))
    print("------------------")

def main(): 
    df = pd.read_csv("data/sample.csv", 
                     skipinitialspace=True, 
                     index_col=0)
    print(df)

    # some standard dataframe methods    
    # the index
    inspect(df.index)

    # the column headings
    inspect(df.columns)
    print(type(df.columns))
    
    # the values of the dataset
    inspect(df.values)
    inspect(df.values[0])
    inspect(df.values[0, 0])

    print(list(df.index))   # convert index to a list    
    print(list(df.columns)) # convert columns to a list
    # extracting a single column can create a new dataframe or a series
    a = df[['County']]    # list parameter => returns a dataset
    print(f"{df[['County']]} returns: \n\t{type(a)}")
    
    b = df['County']      # scalar parameter => returns a series
    print(b)
    print(f"df['County'] returns: \n\t{type(b)}")
        
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
