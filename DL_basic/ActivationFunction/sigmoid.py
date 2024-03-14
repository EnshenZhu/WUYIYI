import numpy as np
import matplotlib.pyplot as plt


def sigmoid(x, beta=1):
    return 1 / (1 + np.exp(-beta * x))


X = np.random.rand(100) * 10 - 5
y = sigmoid(X, beta=5)

plt.scatter(X, y)
plt.show()
