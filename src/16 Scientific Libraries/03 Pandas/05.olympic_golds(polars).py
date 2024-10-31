import os; os.system("clear")
'''
This is the same example as earlier, except we are using Polars to do the computations
'''

import pandas as pd
import polars as pl
pd.set_option('display.width', 100)

def main():
    # read in medal table (n.b. delimiters contain at least 2 spaces and sometimes a bracket) 
    medal_table = pd.read_csv("data/olympics_2012_medal_table.txt",
                               engine = 'python',
                               skiprows = 1,
                               sep = '[ )(]{2,}')
    # convert to polars
    medal_table = pl.from_pandas(medal_table)

    # get number of Korean Golds
    korean_golds = (medal_table                          
                        .filter(pl.col("Id") == "KOR")
                        .select(["Gold"])[0,0])
    print(f"South Korea earned {korean_golds} golds")
    
    print("\nCountries with more golds than South Korea:")
    result = (medal_table
                    .filter(pl.col("Gold") > korean_golds)
                    .select(["Country", "Gold"]))
    pl.Config.set_tbl_hide_dataframe_shape(True)
    pl.Config.set_tbl_formatting('NOTHING')
    pl.Config.set_tbl_hide_column_data_types(True)
    print(result)
main()
