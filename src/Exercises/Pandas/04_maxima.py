'''
Use Pandas to read the file "../MiniProject/wtk_site_metadata.csv"
Print out the row with the largest 'longitude'.
'''

import pandas as pd

df = pd.read_csv("../MiniProject/wtk_site_metadata.csv")
df = df[df['longitude'] == df['longitude'].max()]
series = df['longitude']
print(f"Max longitude: {series.to_string(index=False)}")