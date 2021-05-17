import pandas as pd
pd.set_option('display.precision', 1)
pd.set_option('display.width', None)        # None means all data displayed
pd.set_option('display.max_rows', None)

'''
Pandas 2D dataset are called dataframe.
This example shows several methods of the dataframe.
'''

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
    pd.set_option('display.width', 80)
    print(df.head())       # first five rows
    print(df.tail())       # last five rows
    print(df.sample(5))    # random sample of rows
    print(df.shape)        # number of rows/columns in a tuple
    print(df.describe())   # calculates measures of central tendency
    df.info()              # memory footprint and datatypes

    tmax = df.sort_values('tmax', axis=0, ascending=False)
    pd.set_option('display.max_rows', 20)
    print(tmax)
main()
