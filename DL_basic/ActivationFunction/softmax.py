import numpy as np
import matplotlib.pyplot as plt


def softmax(x, beta=1):
    exp_x = np.exp(beta * (x - np.max(x)))
    return exp_x / exp_x.sum(axis=0, keepdims=True)


X = np.random.rand(100) * 10 - 5
y = softmax(X, beta=1)

print(y.sum(axis=0, keepdims=True))

plt.scatter(X, y)
plt.show()
