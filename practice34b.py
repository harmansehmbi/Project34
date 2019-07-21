import numpy as np
import torch
print(torch.__version__)


print(">> Create Tensor in PyTorch")
# Tensor in n-D Array in PyTorch

X = torch.rand(10, 3, dtype=torch.float)
print(X)
print(type(X))


ndArray = np.zeros(5)
print(ndArray)

