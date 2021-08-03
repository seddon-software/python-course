'''
Use Pandas to read the file "../MiniProject/wtk_site_metadata.csv"
Work with the dataframe 'Rhode Island' as in the previous exercise with the
extra column called 'power'.
Reorder the columns such that the first three columns are 'capacity_factor',
'wind_speed' and 'power' and print the first 5 rows of the dataframe.
'''
import pandas as pd

pd.set_option('display.precision', 2)
pd.set_option('display.width', None)
pd.set_option('display.max_rows', None)

df = pd.read_csv("../MiniProject/wtk_site_metadata.csv")
df['power'] = df.apply(lambda row:row.capacity_factor*row.wind_speed, raw=True, axis=1)

c = df.columns
df = df[[c[8],c[9],c[-1],*c[:8],*c[10:-1]]]
print(df.head())
