'''
Analyse KNeighbors Accuracy
===========================
KNeighbors takes a parameter "n" to determine the number of neighbours to use for kneighbours queries.  We can
see which value of "n" is best suited to our dataset.

We split the dataset into two parts, one part to train the estimator, the other to check the accuracy of the 
estimator.

We split the dataset into the training set (X_train, Y_train) and a test set (X_test, Y_test) using a test_size:
            X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=test_size, random_state=4)

We pass the training set to the estimator:
            estimator.fit(X_train, Y_train)

Now we predict results for our test set: 
            prediction = estimator.predict(X_test)

and then compare with the actual results (Y_test)
            return metrics.accuracy_score(Y_test, prediction)

Looks as though n=7 gives the best results.
'''

from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import numpy as np

# load iris data set
iris = load_iris()
X = iris.data
Y = iris.target

def predict(K, test_size):
    estimator = KNeighborsClassifier(n_neighbors=K)
    # split data into train and test
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=test_size, random_state=4)
    # train for different values of K
    estimator.fit(X_train, Y_train)
    # predict
    prediction = estimator.predict(X_test)
    # compare with actual
    return metrics.accuracy_score(Y_test, prediction)

# vary K
results = []
test_size = 0.6         # split between training data and prediction
                        # the lower the value the more training points are used
for K in range(1, 26):
    results.append(predict(K, test_size))

plt.gcf().canvas.manager.set_window_title("plot the relationship between K and testing accuracy")
plt.plot(range(1, 26), results)
plt.xlabel(f'Value of K for KNN (test_size={test_size})')
plt.ylabel('Testing Accuracy')
plt.grid()
plt.show()

# vary test_size
results = []
for test_size in np.arange(0.1, 1.0, 0.1):
    results.append(predict(10, test_size))

plt.gcf().canvas.manager.set_window_title("plot the testing accuracy ...")
plt.title("... as we change ratio of \ntraining data and prediction data sets")
plt.plot(np.arange(0.1, 1.0, 0.1), results)
plt.xlabel('Value of test_size (K=10)')
plt.ylabel('Testing Accuracy')
plt.show()


