'''
What’s happening
requires_grad=True tells PyTorch:
“track operations on this tensor so we can compute gradients later.”

You define a function:

y=x
2
+3x+1
y.backward() computes derivative 
dx
dy
	​

What gradient means here

Differentiate:

dx
dy
	​

=2x+3

At x=2:

2(2)+3=7

So:

x.grad = 7
Why it matters

This is the mechanism used to train neural networks: computing “how to adjust parameters to reduce error.”
'''

import torch

x = torch.tensor(2.0, requires_grad=True)

y = x**2 + 3*x + 1
y.backward()

print(x.grad)  # dy/dx at x=2