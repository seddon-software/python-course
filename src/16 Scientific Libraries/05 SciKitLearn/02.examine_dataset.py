import os; os.system("clear")
'''
Examine Dataset
===============
We have a CSV file containing information on a number of irises.  This code reads the CSV file into a Pandas 
dataframe.

We will try to predict the species of new irises based on the 4 key characteristics.  There are 3 different 
species of iris to consider:
            setosa
            versicolor
            virginica
'''

import pandas as pd
pd.set_option('display.width', None)        # None means all data displayed


# load iris data set
iris_df = pd.read_csv("data/iris.csv")

# print whole dataframe
print(iris_df)

# print a sample
print(iris_df.sample(5))

