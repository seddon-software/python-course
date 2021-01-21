'''
Use Pandas to read the file "../MiniProject/wtk_site_metadata.csv"
Create the same dataframe 'Rhode Island' as in the previous exercise.
Now add an extra column called 'power' that is computed as the product of the 
columns 'capacity_factor' and 'wind_speed'.
'''
import pandas as pd

pd.set_option('display.precision', 2)
pd.set_option('display.width', None)
pd.set_option('display.max_rows', None)

df = pd.read_csv("../MiniProject/wtk_site_metadata.csv")
df['power'] = df.apply(lambda row:row.capacity_factor*row.wind_speed, raw=True, axis=1)
print(df)
