'''
Use Pandas to read the file "../MiniProject/wtk_site_metadata.csv"
Create a new dataframe with just the 'longitude' and 'latitude' columns.
'''

import pandas as pd

df = pd.read_csv("../MiniProject/wtk_site_metadata.csv")
df = df[['longitude', 'latitude']]
print(df)
