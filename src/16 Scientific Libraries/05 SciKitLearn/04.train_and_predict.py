'''
Train and Predict
=================
Given that the dataset contains 150 records of irises, we can use it to train our estimator.  To do that, we split
the dataframe into two parts: 
            data:    contains the first 4 columns of the dataframe (the key characteristics)
            species: contains the species (column 5)

We then pass these dataframe to the estimator:
            estimator.fit(data, target)     # train the estimator

We try several different estimators:
            from sklearn.neighbors import KNeighborsClassifier
            from sklearn.linear_model import LogisticRegression

The KNeighborsClassifier estimator is based on the nearest neighbour algorithm, see:
            https://scikit-learn.org/stable/modules/neighbors.html#classification

The LogisticRegression estimator is a little complicated.  Read the docs at:
            https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html 

After we have trained the various estimators, we introduce 3 new irises:
            iris1 = [4.1, 3.1, 1.8, 0.5]
            iris2 = [6.9, 3.5, 3.5, 2.5]
            iris3 = [6.7, 2.0, 5.0, 1.6] 

The estimators can now predict results for the 3 unclassified iris
            estimator.predict([iris1, iris2, iris3])

We would hope that all the estimators give he same predictions, but as you will see there is a slight 
disagreement about the species of iris3.
'''

import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression

# target_names = {'setosa':0, 'versicolor':1, 'virginica':2}
iris_df = pd.read_csv("data/iris.csv")
print(f"Shape of dataset: {iris_df.shape}")

# create 2 new dataframes to pass to the estimator
#     data:   contains the first 4 columns of the dataframe
#     species: contains the species (column 5)
data = iris_df.iloc[:,[0,1,2,3]]
species = iris_df.iloc[:,[4]]

# define data for 3 unclassified iris
iris1 = [4.1, 3.1, 1.8, 0.5]
iris2 = [6.9, 3.5, 3.5, 2.5]
iris3 = [6.7, 2.0, 5.0, 1.6] 

def predict(estimator, message, data, species):
    theSpecies = np.ravel(species)          # must be converted to a 1D array
    estimator.fit(data.to_numpy(), theSpecies)       # train the estimator

    # now predict results for the 3 unclassified iris
    print(message, estimator.predict([iris1, iris2, iris3])) # estimate

# predict with different estimators and parameters
print("Try different algorithms to predict the species of the 3 irises")
predict(KNeighborsClassifier(n_neighbors=1), "KNeighbors(K=1):", data, species)
predict(KNeighborsClassifier(n_neighbors=3), "KNeighbors(K=3):", data, species)
predict(KNeighborsClassifier(n_neighbors=5), "KNeighbors(K=5):", data, species)
predict(LogisticRegression(solver='lbfgs', max_iter=150), "LogisticRegression:", data, species)
