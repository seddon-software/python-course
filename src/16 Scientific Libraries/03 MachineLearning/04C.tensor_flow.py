import pandas as pd
import numpy as np
import tensorflow as tf

# -----------------------
# Load dataset
# -----------------------
iris_df = pd.read_csv("data/iris.csv")
print(f"Shape of dataset: {iris_df.shape}")

print(iris_df)

# -----------------------
# Split data and labels
# -----------------------
data = iris_df.iloc[:, [0, 1, 2, 3]].values.astype(np.float32)
species = iris_df.iloc[:, 4].values

# encode labels
label_map = {'setosa': 0, 'versicolor': 1, 'virginica': 2}
species = np.array([label_map[label] for label in species], dtype=np.int64)

# -----------------------
# Define model
# -----------------------
model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation='relu', input_shape=(4,)),
    tf.keras.layers.Dense(3)  # logits
])

# -----------------------
# Loss and optimizer
# -----------------------
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
optimizer = tf.keras.optimizers.Adam(learning_rate=0.01)

# -----------------------
# Training loop
# -----------------------
data_tensor = tf.convert_to_tensor(data)
species_tensor = tf.convert_to_tensor(species)

for epoch in range(101):

    with tf.GradientTape() as tape:
        outputs = model(data_tensor, training=True)
        loss = loss_fn(species_tensor, outputs)

    grads = tape.gradient(loss, model.trainable_variables)
    optimizer.apply_gradients(zip(grads, model.trainable_variables))

    if epoch % 10 == 0:
        print(f"Epoch {epoch}, Loss: {loss.numpy():.4f}")

# new samples
iris1 = [4.1, 3.1, 1.8, 0.5]
iris2 = [6.9, 3.5, 3.5, 2.5]
iris3 = [6.7, 2.0, 5.0, 1.6]

new_data = tf.convert_to_tensor([iris1, iris2, iris3], dtype=tf.float32)

# prediction (no_grad equivalent is simply inference mode)
outputs = model(new_data, training=False)

predicted = tf.argmax(outputs, axis=1).numpy()

# map back to species names
reverse_map = {v: k for k, v in label_map.items()}
predicted_species = [reverse_map[int(p)] for p in predicted]

print("Predictions:", predicted_species)
