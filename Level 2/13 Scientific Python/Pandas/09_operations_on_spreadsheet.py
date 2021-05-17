import pandas as pd
import pylab as pl
pd.set_option('display.precision', 1)
pd.set_option('display.width', 100)

def main(): 
    df = pd.read_excel('data/orders.xlsx', 'SalesOrders')
    print(df)
    
    # caculate sum of Units
    print( f"sum of 'Units' column = {df['Units'].sum(axis=0)}" )
    
    # calculate date range
    dateRange = df['OrderDate'].max() - df['OrderDate'].min() 
    print(f"date range = {dateRange}")
main()

