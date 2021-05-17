'''
Use Pandas to read the file "../MiniProject/wtk_site_metadata.csv"
Print column names.
'''
import pandas as pd

df = pd.read_csv("../MiniProject/wtk_site_metadata.csv")
for column in df.columns:
    print(column)
    
