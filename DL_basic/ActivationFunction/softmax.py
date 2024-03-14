import numpy as np
import matplotlib.pyplot as plt


def softmax(x):
    exp_x = np.exp(x)
    return exp_x / exp_x.sum(axis=0, keepdims=True)


x = np.random.rand(500) * 50 - 25
y = softmax(x)

plt.scatter(x, y)
plt.show()
