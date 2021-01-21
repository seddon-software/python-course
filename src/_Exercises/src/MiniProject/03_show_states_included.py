import pandas as pd

# read in the data
df = pd.read_csv("wtk_site_metadata.csv")

# convert to a series, removing entries where the state is unknown
series = df['State'][df['State'] != 'Unknown']
series = series.drop_duplicates()

# print as a Numpy array
print(series.values)
