# -*- coding: utf-8 -*-
# CODE BORROWED FROM EXAMPLE CODE ON https://pytorch.org/tutorials/beginner/pytorch_with_examples.html

import torch
import math
import matplotlib.pyplot as plt
import numpy as np

dtype = torch.float
device = torch.device("cpu")
# device = torch.device("cuda:0") # Uncomment this to run on GPU

# Create random input and output data
x = np.linspace(-math.pi, math.pi, 2000)
x = torch.from_numpy(x)
y = torch.sin(x)

# Randomly initialize weights
a = torch.randn((), device=device, dtype=dtype)
b = torch.randn((), device=device, dtype=dtype)
c = torch.randn((), device=device, dtype=dtype)
d = torch.randn((), device=device, dtype=dtype)

learning_rate = 1e-6
for t in range(2000):
    # Forward pass: compute predicted y
    y_pred = a + b * x + c * x ** 2 + d * x ** 3

    # Compute and print loss
    loss = (y_pred - y).pow(2).sum().item()

    # Backprop to compute gradients of a, b, c, d with respect to loss
    grad_y_pred = 2.0 * (y_pred - y)
    grad_a = grad_y_pred.sum()
    grad_b = (grad_y_pred * x).sum()
    grad_c = (grad_y_pred * x ** 2).sum()
    grad_d = (grad_y_pred * x ** 3).sum()

    # Update weights using gradient descent
    a -= learning_rate * grad_a
    b -= learning_rate * grad_b
    c -= learning_rate * grad_c
    d -= learning_rate * grad_d


print(f'Result: y = {a.item()} + {b.item()} x + {c.item()} x^2 + {d.item()} x^3')

x = x.tolist()
true_y = y.tolist()
pred_y = [a.item() + b.item()*this_x + c.item()*this_x**2 + d.item()*this_x**3 for this_x in x]

plt.plot(x, true_y, label='True Y')
plt.plot(x, pred_y, label='Pred Y')
plt.legend()
plt.show()

