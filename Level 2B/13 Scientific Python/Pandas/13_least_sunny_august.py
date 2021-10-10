import pandas as pd
import pylab as pl
import numpy as np
pd.set_option('display.precision', 1)
pd.set_option('display.width', 100)

    
def main(): 
    # set column names and read in data from file
    column_names = ['year', 'month', 'tmax', 'tmin', 'air-frost-days', 'rain(mm)', 'sun(hours)', 'comment']
    oxford_data = pd.read_csv("data/oxford2.txt", 
                              engine = 'python', 
                              skiprows = 7, 
                              names = column_names, 
                              na_values = ['---'], 
                              skipinitialspace = True, 
                              sep = '[*# ]+')

    df = oxford_data
    df = df[df['month'] == 8][['year', 'sun(hours)']]
    df = df.dropna()    # remove entries where sun(hours) not recorded
    df = df.sort_values('sun(hours)', ascending=False)
    # results:
    print(f"\nMinimum sun(hours) in August for Oxford since {df['year'].min()}:", end = " ")
    print(f"{df['sun(hours)'].min()} hours in {df['year'].iloc[-1]}, \n")

if __name__ == "__main__":
    main()
