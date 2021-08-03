'''
Use Pandas to read the file "../MiniProject/wtk_site_metadata.csv"
Create the same dataframe 'Rhode Island' as in the previous exercise.
Print the dataframe without the index, display every row to a precision of 2
decimal places
'''

import pandas as pd
pd.set_option('display.precision', 2)
pd.set_option('display.width', None)
pd.set_option('display.max_rows', None)

df = pd.read_csv("../MiniProject/wtk_site_metadata.csv")
df = df[df['State'] == 'Rhode Island']
df = df[['longitude', 'latitude']]
df = df.reset_index()
df.drop(['index'], axis = 1, inplace = True)
print(f"Rhode Island dataframe:\n {df.to_string(index=False)}")
