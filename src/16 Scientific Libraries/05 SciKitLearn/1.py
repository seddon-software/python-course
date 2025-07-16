import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
import numpy as np

# Load the dataset
#df = pd.read_csv('https://raw.githubusercontent.com/fenago/datasets/main/iris.csv')
df = pd.read_csv("data/iris.csv")

# Display the first few rows of the dataset
print(df.head())

# Display the column names
print(df.columns)

# Handle missing values if necessary
df = df.dropna()

# Separate input features and target variable
X = df.drop(columns=['species'])  # 'species' is the target column
y = df['species'].values

# Encode the target variable y (Flower)
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)  # Converts the three flower types into 0, 1, or 2

# Check the number of features
n_features = X.shape[1]

# Split into train and test datasets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# Define the model
model = Sequential()
model.add(Dense(10, activation='relu', input_shape=(n_features,)))
model.add(Dense(8, activation='relu'))
model.add(Dense(3, activation='softmax'))  # 3 neurons for 3 classes (Iris-setosa, Iris-versicolor, Iris-virginica)

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=150, batch_size=32, verbose=0)

# Evaluate the model
loss, acc = model.evaluate(X_test, y_test, verbose=0)
print('Test Accuracy: %.3f' % acc)

# Example prediction
# iris1 = [4.1, 3.1, 1.8, 0.5, 3]
# iris2 = [6.9, 3.5, 2.5, 2.5, 4]  
# iris3 = [6.7, 3.0, 5.2, 2.3, 5] 
iris1 = [4.1, 3.1, 1.8, 0.5]
iris2 = [6.9, 3.5, 2.5, 2.5]  
iris3 = [6.7, 3.0, 5.2, 2.3] 
#sample = np.array([[5.0, 3.6, 1.4, 0.2]])  # Example input for a new flower
sample = np.array([iris1, iris2, iris3])
prediction = model.predict(sample)

# Convert the prediction probabilities into a class label
predicted_class = np.argmax(prediction, axis=1)
print('Predicted class:', predicted_class)