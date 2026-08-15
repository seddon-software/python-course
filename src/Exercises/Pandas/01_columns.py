'''
Use Pandas to read the file "wtk_site_metadata.csv"
Print column names.
'''
import pandas as pd

df = pd.read_csv("wtk_site_metadata.csv")
for column in df.columns:
    print(column)
    
