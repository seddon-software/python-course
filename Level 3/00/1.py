'''
If you want the absolute simplest mental model:

tensors = arrays
autograd = automatic derivatives
nn.Module = model container
optimizer = updates weights

What this demonstrates

This is just NumPy-style array work, but in PyTorch.

torch.tensor(...) creates a tensor (multi-dimensional array).
x + y does element-wise addition → [5, 7, 9]
x * y does element-wise multiplication → [4, 10, 18]
'''

import torch

x = torch.tensor([1.0, 2.0, 3.0])
y = torch.tensor([4.0, 5.0, 6.0])

print(x + y)
print(x * y)
print(x.mean())
