import torch
import torch.nn as nn
import matplotlib.pyplot as plt

m = nn.Softmax(dim=1)
input = torch.randn(20, 3)
output = m(input)

plt.scatter(input, output)
plt.show()
