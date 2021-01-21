import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_rows', None)

sns.set(style="whitegrid", palette="muted")

# Load the example iris dataset
#iris = sns.load_dataset("iris")

iris_df = pd.read_csv("data/iris.csv")

# "Melt" the dataset
#iris_df = pd.melt(iris_df, id_vars="species", var_name="measurement",
iris_df = pd.melt(iris_df, id_vars="species", 
                  var_name='measurement', value_name='cm') 
print(iris_df.sample(20))
print(iris_df)

# Draw a categorical scatterplot to show each observation
sns.swarmplot(x="measurement", 
              y="cm", 
              hue="species",
              palette=["r", "c", "y"], 
              data=iris_df)
plt.show()
