import os; os.system("clear")
'''
You can store Pandas dataframes in HDF5 files.  In this example we read two separate text files (from the Pandas chapter)
into memory as dataframes.  The dataframes are then written to the same HDF5 file:
            data/metoffice

Each dataframe is written with a different key: ("oxford", "lerwick").  Note that we write the first dataframe (mode='w'), but append
the second dataframe (mode='a).

Once both datframes have been written, we can read them back individually using:
            pd.read_hdf()

and supplying the appropriate key.
'''

import h5py
import pandas as pd


OXFORD_DATA = "data/oxford_2022.txt"
LERWICK_DATA = "data/lerwick.txt"
HDF5_FILE = "data/met_office.h5"

def read_met_data(fileName):
    column_names = ['year', 'month', 'tmax', 'tmin', 'air-frost-days', 'rain(mm)', 'sun(hours)', 'comment']
    df = pd.read_csv(f"{fileName}", 
                                engine = 'python', 
                                skiprows = 7, 
                                names = column_names,     
                                na_values = ['---'], 
                                skipinitialspace = True, 
                                sep = '[*# ]+')
    return df

oxford_df = read_met_data(OXFORD_DATA)
try:
    oxford_df.to_hdf(HDF5_FILE, key='oxford', mode='w') 
except Exception as e:
    print(e)
lerwick_df = read_met_data(LERWICK_DATA)
lerwick_df.to_hdf(HDF5_FILE, key='lerwick', mode='a') 

# this will only read the lerwick dataframe.  The oxford dataframe does NOT get read into memory here. 
lerwick_df2 = pd.read_hdf(HDF5_FILE, key="lerwick")
print(lerwick_df2)

# now read the oxford dataframe
oxford_df2 = pd.read_hdf(HDF5_FILE, key="oxford")
print(oxford_df2)

# check for differences
def isSame(name, df1, df2):
    diffs = df1.compare(df2)
    if diffs.empty:
        print(f"{name} dataframes are the same")

isSame("lerwick", lerwick_df, lerwick_df2)
isSame("oxford", oxford_df, oxford_df2)
  
