import pandas as pd
import numpy as np

pd.set_option('display.width', None)
pd.set_option('display.precision', 2)

df = pd.read_excel("data/sales.xlsx")
print(df.head())

# print out the head of the data frame
# n.b. cat is accessor object for categorical properties of the Series values
df["Status"] = df["Status"].astype("category")  # enums
df["Status"].cat.set_categories(["won","pending","presented","declined"],inplace=True)
print(df.head())
print("============================================================================================================")

# display the total, average and number of "Price" entries for each Manager-Rep pair
pivot = pd.pivot_table(df,index=["Manager", "Rep"], values = "Price", aggfunc = [np.sum, np.mean, len])
pivot.columns = ['total', 'average', 'number']
print(pivot)

# display the total of "Price" entries for each Manager-Rep pair and give additional columns for each "Product"
print("============================================================================================================")
print(pd.pivot_table(df,index=["Manager", "Rep"], values = "Price", columns = ["Product"], aggfunc = [np.sum]))

# same again, but with nulls filled as zeros
print("============================================================================================================")
print(pd.pivot_table(df,index=["Manager", "Rep"], values = "Price", columns = ["Product"], aggfunc = [np.sum], fill_value = 0))

# move "Product" to index, so we display Manager-Rep-Product for each aggregate function 
print("============================================================================================================")
print(pd.pivot_table(df,
                     index=["Manager", "Rep",  "Product"], 
                     values = ["Price", "Quantity"], 
                     aggfunc = [np.sum, np.mean, len], 
                     fill_value = 0, 
                     margins = True))
# 
# pivot on Manager-Status, but then only display Debra Henley's results
print("============================================================================================================")
table = pd.pivot_table(df,index=["Manager","Status"],columns=["Product"],values=["Quantity","Price"],
               aggfunc={"Quantity":len,"Price":[np.sum,np.mean]},fill_value=0)
print(table.query('Manager == ["Debra Henley"]'))
