'''
Step-by-step:

Forward pass
pred = model(x)
model guesses outputs
Compute loss
compare predictions vs real values
Zero gradients
PyTorch accumulates gradients by default, so reset them
Backward pass
loss.backward() computes gradients:
how much each parameter contributed to error
Update weights
opt.step() adjusts w and b
'''

import torch
import torch.nn as nn

# simple dataset: y = 2x + 1
x = torch.tensor([[1.0], [2.0], [3.0], [4.0]])
y = torch.tensor([[3.0], [5.0], [7.0], [9.0]])

model = nn.Linear(1, 1)
loss_fn = nn.MSELoss()
opt = torch.optim.SGD(model.parameters(), lr=0.01)

for _ in range(200):
    pred = model(x)
    loss = loss_fn(pred, y)

    opt.zero_grad()
    loss.backward()
    opt.step()

print(model.weight.item(), model.bias.item())