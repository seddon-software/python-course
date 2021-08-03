import pandas as pd

# read JSON from file
df = pd.read_json('data.json')
print(df)

# write JSON to csv file
df.to_csv("data.csv")

# read csv file into dataframe
df2 = pd.read_csv("data.csv")

# save dataframe to new JSON file
df2.to_json("data2.json")

