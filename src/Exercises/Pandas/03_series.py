'''
Use Pandas to read the file "wtk_site_metadata.csv"
Create a new series from the 'State' column of the dataframe
and then remove duplicates.
'''

import pandas as pd

df = pd.read_csv("wtk_site_metadata.csv")
series = df['State']
series = series.drop_duplicates()
print(series)

