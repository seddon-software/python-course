'''
Use Pandas to read the file "../MiniProject/wtk_site_metadata.csv"
Create a new dataframe containing rows with state equal to 'Rhode Island'.
Retain the 'longitude' and 'latitude' columns.
Reset the index such that it starts at 1.
'''

import pandas as pd

df = pd.read_csv("../MiniProject/wtk_site_metadata.csv")
df = df[df['State'] == 'Rhode Island']
df = df[['longitude', 'latitude']]
df = df.reset_index()
df.drop(['index'], axis = 1, inplace = True)
print(f"Rhode Island dataframe: {df}")
