import pandas as pd
pd.set_option('display.width', None)        # None means all data displayed


# load iris data set
iris_df = pd.read_csv("data/iris.csv")
print(iris_df)
