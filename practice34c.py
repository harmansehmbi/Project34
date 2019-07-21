import torch
import numpy as np

print(">> Torch Version:",torch.__version__)

X = torch.empty(5, 3)
print(X)
print(type(X)) # Tensor -> is n-D Array in PyTorch and TensorFlow

print()

X = torch.rand(3, 3)
print(X)

print()

X = torch.zeros(5, 5)
print(X)

print()

X = torch.zeros(5, 5, dtype=torch.int)
print(X)







