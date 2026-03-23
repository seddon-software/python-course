import pandas as pd
import numpy as np


df = pd.read_csv("data/football_results.txt", sep=r",\s+", engine="python")
df['Match'] = df.apply(lambda row: row.name%4, raw=False, axis=1)
print(df)
print()

df2 = df.pivot(index='Match', columns='Team', values='Score')
print(df2)
print()

df2 = df.pivot(index='Team', columns='Match', values='Score')
print(df2)
