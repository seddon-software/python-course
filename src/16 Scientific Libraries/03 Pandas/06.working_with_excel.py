# Reading Excel files requires the xlrd library. 
# You can install it via pip (pip install xlrd).

'''
In this example we take a spreadsheet that is published by ONS that contains provisional results of the 2021
census in England and wales.

We show how to 
    1) read in a single sheet of the spreadsheet
    2) modify the column headings
    3) combine pairs of rows
    4) drop unwanted columns
'''

import pandas as pd
import pylab as pl
pd.set_option('display.width', None)        # None means all data displayed
pd.set_option('display.max_rows', None)
EXCEL_FILE="data/census_data.xlsx"
SHEET="P02"

def main(): 
    cols = list(range(1,11))
    df = pd.read_excel(
        io=EXCEL_FILE, 
        sheet_name=SHEET,
        skiprows=7,
        index_col=None,
        usecols=cols)
    # reduce verbocity of column names
    df.columns = df.columns.str.replace(r'(.*) years(.*)\n\[note 12\]', r'\1\2', regex=True)
    print("head of original data: ")
    print(df.head())
    input("Hit a key to combine columns: ")

    def combineRows(df, title, n1, n2):
        df[title] = df.apply(lambda row:row[n1]+row[n2], axis=1, raw=True)
        return df
    
    def dropColumns(df, begin, end):
        cols = list(range(begin, end+1))
        df.drop(df.columns[cols], axis=1, inplace=True)
        return df

    df = combineRows(df, ' 0 to 9', 2, 3)
    df = combineRows(df, '10 to 19', 4, 5)
    df = combineRows(df, '20 to 29', 6, 7)
    df = combineRows(df, '30 to 39', 8, 9)
    df = dropColumns(df, 1, 9)
    print(df.iloc[:30])     # just print out the first 30 rows
main()

