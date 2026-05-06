'''
Plot 3 Unclassified Irises
==========================
Now we have the predictions from the estimators we can plot the new irises and see how good the estimators are.
The new irises are coloured "orange", "lime" and "fuchsia".
'''

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas as pd

colors = ["orange", "green", "blue", "red", "lime", "fuchsia"]
markers = ["o", "o", "o", "D", "D", "D"]
sizes = [10, 10, 10, 100, 100, 100]
labels = ['sepal length', 'sepal width', 'petal length', 'petal width']
target_names = {'setosa':0, 'versicolor':1, 'virginica':2}

iris_df = pd.read_csv("data/iris.csv")
iris_df["target"] = iris_df.apply(lambda row: target_names[row.species], axis=1, raw=False)
iris_df.drop(["species"], axis = 1, inplace = True)
iris1 = [4.1, 3.1, 1.8, 0.5, 3]
iris2 = [6.9, 3.5, 2.5, 2.5, 4]  
iris3 = [6.7, 3.0, 5.2, 2.3, 5] 
df = pd.DataFrame([iris1, iris2, iris3], columns = iris_df.columns) 
iris_df = pd.concat([iris_df, df])

# plot
figure = plt.figure(figsize=(12, 8))

def scatter(subplot, i, j, k):
    def doScatter(row):
        n = int(row[4])          
        ax.scatter(row[i], row[j], row[k],   
                   c=colors[n], 
                   marker=markers[n],
                   s=sizes[n])

    ax = figure.add_subplot(subplot, projection='3d')
    ax.set_xlabel(labels[i])
    ax.set_ylabel(labels[j])
    ax.set_zlabel(labels[k])
    iris_df.apply(doScatter, axis=1, raw=True)

    # print variety names on plot
    for name, label in [('Setosa', 0),
                        ('Versicolour', 1),
                        ('Virginica', 2)]:
        x = iris_df[iris_df['target']==label][iris_df.columns[i]].mean()
        y = iris_df[iris_df['target']==label][iris_df.columns[j]].mean()
        z = iris_df[iris_df['target']==label][iris_df.columns[k]].mean()
        ax.text3D(x, y, z, name,
                color='saddlebrown', fontsize=14,
                horizontalalignment='center',
                bbox=dict(alpha=.2, edgecolor='w', facecolor='w'))

scatter(221, 0, 1, 2)
scatter(222, 0, 1, 3)
scatter(223, 0, 2, 3)
scatter(224, 1, 2, 3)
plt.show()
