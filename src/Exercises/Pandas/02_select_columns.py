'''
Use Pandas to read the file "wtk_site_metadata.csv"
Create a new dataframe with just the 'longitude' and 'latitude' columns.
'''

import pandas as pd

df = pd.read_csv("wtk_site_metadata.csv")
df = df[['longitude', 'latitude']]
print(df)
