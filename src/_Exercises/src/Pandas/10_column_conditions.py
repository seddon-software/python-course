'''
Use Pandas to read the file "../MiniProject/wtk_site_metadata.csv"
Work with the dataframe 'Rhode Island' as in the previous exercise with the
extra column called 'power' and the column headings resorted.
Create a new sorted dataframe with rows from the 'Rhode Island' dataframe with
a 'power' greater than 3.
'''
import pandas as pd

pd.set_option('display.precision', 2)
pd.set_option('display.width', None)
pd.set_option('display.max_rows', None)

df = pd.read_csv("../MiniProject/wtk_site_metadata.csv")
df['power'] = df.apply(lambda row:row.capacity_factor*row.wind_speed, raw=True, axis=1)

c = df.columns
df = df[[c[8],c[9],c[-1],*c[:8],*c[10:-1]]]

df = df[df['power'] > 3.0]
df.sort_values('power', axis=0, ascending=False, inplace=True)
print(df)
