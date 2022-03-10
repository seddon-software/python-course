import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression

target_names = {'setosa':0, 'versicolor':1, 'virginica':2}
iris_df = pd.read_csv("data/iris.csv")
print(iris_df.shape)

# add a numerical column based on target names
iris_df["target"] = iris_df.apply(
    lambda row: target_names[row.species], axis=1, raw=False)
iris_df.drop(["species"], axis = 1, inplace = True)

# create 2 new dataframes to pass to the estimator
#     data:   contains the first 4 columns of the dataframe
#     target: contains the species number (column 5)
data = iris_df.iloc[:,[0,1,2,3]]
target = iris_df.iloc[:,[4]]

# define dat for 3 unclassified iris
iris1 = [4.1, 3.1, 1.8, 0.5]
iris2 = [6.9, 3.5, 3.5, 2.5]
iris3 = [6.7, 2.0, 5.0, 1.6] 

def predict(estimator, message):
    estimator.fit(data, target)     # train the estimator
    # now predict results for the 3 unclassified iris
    print(message, estimator.predict([iris1, iris2, iris3])) # estimate

# predict with different estimators and parameters
predict(KNeighborsClassifier(n_neighbors=1), "KNeighbors(K=1):")
predict(KNeighborsClassifier(n_neighbors=3), "KNeighbors(K=3):")
predict(KNeighborsClassifier(n_neighbors=5), "KNeighbors(K=5):")
predict(LogisticRegression(solver='lbfgs', multi_class='auto', max_iter=150), "LogisticRegression:")
