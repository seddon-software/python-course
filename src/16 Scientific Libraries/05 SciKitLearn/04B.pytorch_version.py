'''
Train and Predict
=================
Given that the dataset contains 150 records of irises, we can use it to train our estimator.  To do that, we split
the dataframe into two parts: 
            data:    contains the first 4 columns of the dataframe (the key characteristics)
            species: contains the species (column 5)
'''

import pandas as pd
import numpy as np
import torch
import torch.nn as nn  # base class for all neural networks in PyTorch
import torch.optim as optim

# load dataset
iris_df = pd.read_csv("data/iris.csv")
print(f"Shape of dataset: {iris_df.shape}")

print(iris_df)
# split data and species
data = iris_df.iloc[:, [0,1,2,3]].values.astype(np.float32)        # first 4 columns
species = iris_df.iloc[:, 4].values                                   # only column 5

# encode labels (setosa=0, versicolor=1, virginica=2)
label_map = {'setosa': 0, 'versicolor': 1, 'virginica': 2}
# convert the species array to numeric form using the label_map
species = np.array([label_map[label] for label in species], dtype=np.int64)

# convert to tensors
data_tensor = torch.tensor(data)
species_tensor = torch.tensor(species)

# define model
'''A neuron takes in numbers, processes them, and produces an output. It does this in three main steps:

Input + weights
Each input is multiplied by a weight (a learned parameter that represents importance).
Summation + bias
The weighted inputs are added together, along with a bias term.
Activation function
The result is passed through a function that introduces non-linearity (this allows the network to learn complex patterns).
'''
class IrisModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(4, 10),
            # 4 → input dimension
            # 10 → hidden neurons (chosen design choice)
            nn.ReLU(),
            nn.Linear(10, 3)  # 3 species (logits)
        )

    def forward(self, x):
        return self.model(x)

model = IrisModel()

# loss and optimizer
'''
Compares the model’s predicted probabilities with the true class labels
Produces a single number (the loss) indicating how wrong the model is
'''
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.01) 

# training loop
for epoch in range(101):
    optimizer.zero_grad() # clears previously computed gradients (because PyTorch accumulates gradients by default)
    outputs = model(data_tensor) # feeds input data into the model and produces predictions (outputs)
    loss = criterion(outputs, species_tensor) # compares predictions to true labels and returns a single scalar (how wrong the model is)
    loss.backward() # computes gradients of the loss with respect to each parameter
    optimizer.step() # uses gradients to adjust weights (to reduce future loss)

    if epoch % 10 == 0:
        print(f"Epoch {epoch}, Loss: {loss.item():.4f}")  # see how the loss changes with training

# new samples
iris1 = [4.1, 3.1, 1.8, 0.5]
iris2 = [6.9, 3.5, 3.5, 2.5]
iris3 = [6.7, 2.0, 5.0, 1.6]

new_data = torch.tensor([iris1, iris2, iris3], dtype=torch.float32)

# prediction
'''
SciKitLearn gave (K=7 was most accurate): 
KNeighbors(K=1): ['setosa' 'versicolor' 'versicolor']
KNeighbors(K=3): ['setosa' 'versicolor' 'virginica']
KNeighbors(K=5): ['setosa' 'versicolor' 'versicolor']
KNeighbors(K=7): ['setosa' 'versicolor' 'versicolor']
LogisticRegression: ['setosa' 'versicolor' 'virginica']
'''
model.eval()
with torch.no_grad():
    outputs = model(new_data)   # largest value in a row = the model’s strongest guess; index of that value = the predicted species
    predicted = outputs.argmax(dim=1)
    
# map back to species names
reverse_map = {v: k for k, v in label_map.items()}
predicted_species = [reverse_map[int(p)] for p in predicted]

print("Predictions:", predicted_species)
